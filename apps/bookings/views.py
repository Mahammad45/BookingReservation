from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets , generics , permissions

from apps.bookings.models import Booking
from apps.bookings.serializers import BookingSerializer

class BookingListCreatedAPIView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAdminUser]