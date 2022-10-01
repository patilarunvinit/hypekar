from .models import booking
from rest_framework import serializers




class bookingserializer(serializers.Serializer):
    email = serializers.CharField(max_length=50)
    customer_name = serializers.CharField(max_length=60)
    customer_address = serializers.CharField(max_length=200)
    service_address = serializers.CharField(max_length=200)
    brand = serializers.CharField(max_length=60)
    model = serializers.CharField(max_length=100)
    service_type = serializers.CharField(max_length=60)
    time_slot = serializers.CharField(max_length=100)
    date = serializers.CharField(max_length=100)

    class Meta:
        model = booking
        fields = ("email", "customer_name", "customer_address", "service_address", "brand", "model", "service_type","time_slot","date")

    def create(self, validated_data):
        return booking.objects.create(**validated_data)