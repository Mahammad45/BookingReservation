from django.db import models

# Create your models here.

class Payment(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'