from .models import contanctpage, cars, mycar
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



class carsserializer(serializers.Serializer):
    brand = serializers.CharField(max_length=60)
    model_name = serializers.CharField(max_length=60)


    class Meta:
        model = cars
        fields = ("brand","model_name")

    def create(self, validated_data):
        return cars.objects.create(**validated_data)



class cars2serializer(serializers.Serializer):
    brand = serializers.CharField(max_length=60)

    class Meta:
        model = cars
        fields = ("brand")

    def create(self, validated_data):
        return cars.objects.create(**validated_data)




class cars3serializer(serializers.Serializer):
    model_name = serializers.CharField(max_length=60)

    class Meta:
        model = cars
        fields = ("model_name")

    def create(self, validated_data):
        return cars.objects.create(**validated_data)


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