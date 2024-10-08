from django.db import models

# Create your models here.



class Hotels(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'
    
class Rooms(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'