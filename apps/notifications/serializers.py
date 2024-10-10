from rest_framework import serializers

from apps.notifications.models import Notifications


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
        