from django.urls import path
from apps.reviews.views import ReviewsListCreatedAPIView

urlpatterns = [
    path('reviews/', ReviewsListCreatedAPIView.as_view(), name='reviews-list'),
    path('reviews/<int:pk>/', ReviewsListCreatedAPIView.as_view(), name='reviews-detail'),
]
