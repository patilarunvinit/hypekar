from .models import mycar
from rest_framework import serializers




class mycarserializer(serializers.Serializer):
    email = serializers.CharField(max_length=50)
    brand = serializers.CharField(max_length=60)
    model_Name = serializers.CharField(max_length=60)
    vehicle_number = serializers.CharField(max_length=60)
    year_Of_Model = serializers.IntegerField()
    fuel_Type = serializers.CharField(max_length=20)
    mobile_number = serializers.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        model = mycar
        fields = ("email", "brand", "model_Name", "vehicle_number", "year_Of_Model", "fuel_Type", "mobile_number")

    def create(self, validated_data):
        return mycar.objects.create(**validated_data)





class mycarbrandserializer(serializers.Serializer):
    brand = serializers.CharField(max_length=60)


    class Meta:
        model = mycar
        fields = ("brand")

    def create(self, validated_data):
        return mycar.objects.create(**validated_data)


class mycarmodelserializer(serializers.Serializer):
    model_Name = serializers.CharField(max_length=60)


    class Meta:
        model = mycar
        fields = ("model_Name")

    def create(self, validated_data):
        return mycar.objects.create(**validated_data)