from rest_framework import serializers
from .models.payment import Payment 
from tourist.serializers import TouristSerializer
from .models.site import Site 


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class PaymentReportSerializer(serializers.ModelSerializer):
    tourist = TouristSerializer()
    class Meta:
        model = Payment
        fields = ["tourist", "amount_paid"]


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = "__all__"
