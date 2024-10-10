from django.urls import path
from apps.users.views import UserProfileListCreatedAPIView

urlpatterns = [
    path('profiles/', UserProfileListCreatedAPIView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', UserProfileListCreatedAPIView.as_view(), name='profile-detail'),
]