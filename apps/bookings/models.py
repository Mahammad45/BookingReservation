from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'