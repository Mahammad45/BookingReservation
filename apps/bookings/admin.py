from django.contrib import admin

# Register your models here.


from apps.bookings.models import Booking

admin.site.register(Booking)

admin.site.index_title = "Hotel Reservation"
admin.site.site_header = "Hotel Reservation"
admin.site.site_title = "Hotel Reservation"