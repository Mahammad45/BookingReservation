from rest_framework import serializers

from apps.reviews.models import Reviews

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'