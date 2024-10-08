from django.db import models

# Create your models here.

class Notifications(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'