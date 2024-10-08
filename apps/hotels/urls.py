from django.urls import path
from apps.hotels.views import(
    HotelsListCreatedAPIView,RoomsListCreatedAPIView
)

urlpatterns = [
    path('hotels/',HotelsListCreatedAPIView.as_view(),name='hotels'),
    path('rooms/',RoomsListCreatedAPIView.as_view(),name='rooms'),
    path('hotels/<int:pk>/', HotelsListCreatedAPIView.as_view(), name='hotels-detail'),
    path('rooms/<int:pk>/', RoomsListCreatedAPIView.as_view(), name='rooms-detail'),
    path('hotels/<int:pk>/update/', HotelsListCreatedAPIView.as_view(), name='hotels-update'),
    path('rooms/<int:pk>/update/', RoomsListCreatedAPIView.as_view(), name='rooms-update'),
    path('hotels/<int:pk>/delete/', HotelsListCreatedAPIView.as_view(), name='hotels-delete'),
    path('rooms/<int:pk>/delete/', RoomsListCreatedAPIView.as_view(), name='rooms-delete'),
    
]