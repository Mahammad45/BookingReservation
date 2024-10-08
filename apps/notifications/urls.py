from django.urls import path
from apps.notifications.views import NotificationList, NotificationDetail, NotificationCreate, NotificationUpdate, NotificationDelete

urlpatterns = [
    path('notifications/', NotificationList.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', NotificationDetail.as_view(), name='notification-detail'),
    path('notifications/create/', NotificationCreate.as_view(), name='notification-create'),
    path('notifications/<int:pk>/update/', NotificationUpdate.as_view(), name='notification-update'),
    path('notifications/<int:pk>/delete/', NotificationDelete.as_view(), name='notification-delete'),
]