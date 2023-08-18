from .models import Customer, ServiceRequest,TrackStatus
from rest_framework import serializers

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ('account','customer','Service_Type','request_detials','attachment','submitted_at')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class TrackStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackStatus
        fields = '__all__'

