from django.urls import path
from apps.users.views import UserProfileListCreatedAPIView

urlpatterns = [
    path('profiles/', UserProfileListCreatedAPIView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', UserProfileListCreatedAPIView.as_view(), name='profile-detail'),
    path('profiles/<int:pk>/update/', UserProfileListCreatedAPIView.as_view(), name='profile-update'),
    path('profiles/<int:pk>/delete/', UserProfileListCreatedAPIView.as_view(), name='profile-delete'),
]