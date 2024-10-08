from django.contrib import admin

# Register your models here.

from apps.reviews.models import Review

admin.site.register(Review)

admin.site.site_header = "Review Admin"
admin.site.site_title = "Review Admin"
admin.site.index_title = "Welcome to Review Admin"