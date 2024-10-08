from django.contrib import admin


# Register your models here.


from apps.payments.models import Payment

admin.site.register(Payment)

admin.site.index_title = "Hotel Reservation"
admin.site.site_title = "Hotel Reservation"
admin.site.site_header = "Hotel Reservation"