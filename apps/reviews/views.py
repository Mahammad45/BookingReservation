from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets , generics , permissions

from apps.reviews.models import Reviews
from apps.reviews.serializers import ReviewsSerializer

class ReviewsListCreatedAPIView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReviewsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.IsAdminUser]
    