from django.contrib import admin

# Register your models here.

from apps.notifications.models import Notifications

admin.site.register(Notifications)

admin.site.site_header = 'Hotel Reservation'
admin.site.site_title = 'Hotel Reservation'
admin.site.index_title = 'Hotel Reservation'