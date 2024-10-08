from rest_framework import serializers
from apps.hotels.models import Hotels, Rooms

class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'