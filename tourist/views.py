# Python/Django imports
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, mixins

# Local app imports
from .serializers import TouristSerializer
from .models.tourist import Tourist


class TouristGeneralViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """Provide Create functionality"""

    queryset = Tourist.objects.all()
    serializer_class = TouristSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"


class TouristAuthViewSet(
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    """Provide Retrieve, update and delete functionality"""

    queryset = Tourist.objects.all()
    serializer_class = TouristSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
