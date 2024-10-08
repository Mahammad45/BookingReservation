from rest_framework import serializers
from apps.users.models import UserProfiles

class UserProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = '__all__'
        