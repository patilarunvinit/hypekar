from .models import FeedBack
from rest_framework import serializers


class FeedBackserializer(serializers.Serializer):
    email = serializers.CharField(max_length=60)
    description = serializers.CharField()
    rating = serializers.IntegerField()
    location = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)

    class Meta:
        model = FeedBack
        felds = ("email", "description","rating","location","name")

    def create(self, validated_data):
        return FeedBack.objects.create(**validated_data)