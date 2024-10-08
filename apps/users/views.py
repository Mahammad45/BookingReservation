from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets , permissions , generics

from apps.users.models import UserProfiles
from apps.users.serializers import UserProfilesSerializer

class UserProfileListCreatedAPIView(generics.ListCreateAPIView):
    queryset = UserProfiles.objects.all()
    serializer_class = UserProfilesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfiles.objects.all()
    serializer_class = UserProfilesSerializer
    permission_classes = [permissions.IsAdminUser]