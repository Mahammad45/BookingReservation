from django.contrib import admin

# Register your models here.

from apps.users.models import UserProfiles

admin.site.register(UserProfiles)

admin.site.site_header = "Hotel Reservation Admin"
admin.site.site_title = "Hotel Reservation Admin Portal"
admin.site.index_title = "Welcome to Hotel Reservation Admin Portal"