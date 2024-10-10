from django.urls import path
from apps.payments.views import PaymentListCreatedAPIView

urlpatterns = [
    path('payments/', PaymentListCreatedAPIView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentListCreatedAPIView.as_view(), name='payment-detail'),
]