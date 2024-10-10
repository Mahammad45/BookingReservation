from django.urls import path
from apps.hotels.views import HotelsListCreateAPIView, HotelsRetrieveUpdateDestroyAPIView, RoomsListCreateAPIView, RoomsRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('hotels/', HotelsListCreateAPIView.as_view()),
    path('hotels/<int:pk>/', HotelsRetrieveUpdateDestroyAPIView.as_view()),
    path('rooms/', RoomsListCreateAPIView.as_view()),
    path('rooms/<int:pk>/', RoomsRetrieveUpdateDestroyAPIView.as_view()),
    
]