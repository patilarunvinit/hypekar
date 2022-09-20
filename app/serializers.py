from .models import contanctpage
from rest_framework import serializers

class contanctserializer(serializers.Serializer):
    firstName = serializers.CharField(max_length=60)
    lastName = serializers.CharField(max_length=60)
    type = serializers.CharField(max_length=100)
    mobileNumber = serializers.IntegerField()


    class Meta:
        model = contanctpage
        fields = ("firstName","lastName","type","mobileNumber")

    def create(self, validated_data):
        return contanctpage.objects.create(**validated_data)
