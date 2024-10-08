from django.urls import path
from apps.payments.views import PaymentListCreatedAPIView

urlpatterns = [
    path('payments/', PaymentListCreatedAPIView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentListCreatedAPIView.as_view(), name='payment-detail'),
    path('payments/<int:pk>/update/', PaymentListCreatedAPIView.as_view(), name='payment-update'),
    path('payments/<int:pk>/delete/', PaymentListCreatedAPIView.as_view(), name='payment-delete'),
]