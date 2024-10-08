from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets , permissions,generics

from apps.notifications.models import Notification
from apps.notifications.serializers import NotificationSerializer


class NotificationsListCreatedAPIView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

class NotificationsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAdminUser]