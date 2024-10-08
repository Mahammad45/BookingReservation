from django.db import models

# Create your models here.

class Reviews(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'