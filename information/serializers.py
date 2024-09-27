from rest_framework import serializers
from .models import Station, Information

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class InformationSerializer(serializers.ModelSerializer):
    station = StationSerializer()

    class Meta:
        model = Information
        fields = '__all__'
