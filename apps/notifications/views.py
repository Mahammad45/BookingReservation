from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets , permissions,generics

from apps.notifications.models import Notifications
from apps.notifications.serializers import NotificationSerializer


class NotificationsListCreatedAPIView(generics.ListCreateAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

class NotificationsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAdminUser]