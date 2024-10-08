from django.contrib import admin

# Register your models here.

from apps.hotels.models import Hotels , Rooms

admin.site.register(Hotels)
admin.site.register(Rooms)

admin.site.index_title = "Hotel Reservation"
admin.site.site_header = "Hotel Reservation"
admin.site.site_title = "Hotel Reservation"


