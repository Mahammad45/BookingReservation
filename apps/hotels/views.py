from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets, generics , permissions
from apps.hotels.models import Hotels, Rooms
from apps.hotels.serializers import HotelsSerializer , RoomsSerializer

class HotelsListCreatedAPIView(viewsets.ModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer

class RoomsListCreatedAPIView(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class HotelsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer
    permission_classes = [permissions.IsAdminUser]

class RoomsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = [permissions.IsAdminUser]