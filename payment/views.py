# Python/Django imports
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum

# Local app imports
from .serializers import PaymentSerializer, SiteSerializer, PaymentReportSerializer
from .models.payment import Payment
from .models.site import Site 
from tourist.models.tourist import Tourist
from tourist.serializers import TouristSerializer

# Payment views

class PaymentAuthViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    """Provide CRUD functionality"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


class TouristPaymentReportView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = PaymentReportSerializer

    def get(self, request):
        payments = Payment.objects.all()
        data    = self.serializer_class(payments, many=True)
        total_amount = Payment.objects.aggregate(Sum('amount_paid'))
        return Response({
            "tourists": data.data,
            "total_amount": total_amount["amount_paid__sum"]
        }, status = status.HTTP_200_OK)


class ZooPaymentsView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = PaymentSerializer

    def get(self, request):
        payments = Payment.objects.filter(site__name="zoo")
        data    = self.serializer_class(payments, many=True)
        return Response({
            "data": data.data,
        }, status = status.HTTP_200_OK)


class NoSitePaymentsView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = TouristSerializer

    def get(self, request):
        tourists = Tourist.objects.all()
        payments = Payment.objects.all()
        
        no_payment_tourists_list = []
        
        for tourist in tourists:
            if not Payment.objects.filter(tourist=tourist).exists():
                no_payment_tourists_list.append(tourist)
        
        
        data    = self.serializer_class(no_payment_tourists_list, many=True)


        return Response({
            "data": data.data,
        }, status = status.HTTP_200_OK)

# Site views

class SiteViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin
):
    """Provide Retrieve functionality"""

    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"