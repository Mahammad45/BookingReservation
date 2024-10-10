from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets, generics , permissions
from apps.hotels.models import Hotels, Rooms
from apps.hotels.serializers import HotelsSerializer , RoomsSerializer

class HotelsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer
    permission_classes = [permissions.IsAdminUser]


class HotelsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer
    permission_classes = [permissions.IsAdminUser]


class RoomsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = [permissions.IsAdminUser]


class RoomsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = [permissions.IsAdminUser]