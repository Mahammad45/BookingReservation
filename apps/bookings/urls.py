from django.urls import path  
from apps.bookings.views import BookingListCreatedAPIView


urlpatterns = [
    path('bookings/', BookingListCreatedAPIView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingListCreatedAPIView.as_view(), name='booking-detail'),
]