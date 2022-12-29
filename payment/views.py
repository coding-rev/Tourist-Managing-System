# Python/Django imports
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, mixins

# Local app imports
from .serializers import PaymentSerializer, SiteSerializer
from .models.payment import Payment
from .models.site import Site 


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


class SiteViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin
):
    """Provide Retrieve functionality"""

    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"