from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets , permissions , generics
from apps.payments.models import Payment
from apps.payments.serializers import PaymentSerializer

class PaymentListCreatedAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PaymentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAdminUser]