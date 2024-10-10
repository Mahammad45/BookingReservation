from django.urls import path
from apps.notifications.views import NotificationsListCreatedAPIView, NotificationsRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('notifications/', NotificationsListCreatedAPIView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', NotificationsRetrieveUpdateDestroyAPIView.as_view(), name='notification-detail'),
]