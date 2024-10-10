from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API для продуктов",
        default_version='v1',
        description="Документация к API для отслеживания продуктов.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(
            name="Mahammad", 
            url="https://t.me/Though_123",
            email="mahammad6111@gmail.com"
        ),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [

    path('admin/', admin.site.urls),

    path('api-auth/', include('djoser.urls')),
    path('api-auth/', include('djoser.urls.jwt')),
    
    path('api/v1/', include('apps.notifications.urls')),
    path('api/v1/', include('apps.bookings.urls')),
    path('api/v1/', include('apps.users.urls')),
    path('api/v1/', include('apps.payments.urls')),
    path('api/v1/', include('apps.hotels.urls')),
    path('api/v1/', include('apps.reviews.urls')),





    # Swagger

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]