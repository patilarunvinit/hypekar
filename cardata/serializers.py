from .models import  cars
from rest_framework import serializers


class carsserializer(serializers.Serializer):
    brand = serializers.CharField(max_length=60)
    model_name = serializers.CharField(max_length=60)
    basic =serializers.IntegerField()
    standard = serializers.IntegerField()
    premium =serializers.IntegerField()

    class Meta:
        model = cars
        fields = ("brand","model_name","basic","standard","premium")

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