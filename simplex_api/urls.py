from django.urls import path, include
from django.contrib import admin
from simplex_api.views import not_found, app_error
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

handler404 = not_found
handler500 = app_error

schema_view = get_schema_view(
   openapi.Info(
      title="Simplex Ag API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/messages/', include('messages_api.urls')),
    path('api/core/', include('core.urls')),
    path('api/samples/', include('samples.urls')),
    path('api/samples/', include('samples.urls')),
    path('api/equations/', include('equations.urls')),
    path('api/products/', include('products.urls')),
    path('api/rx/', include('recommendations.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #path('api/core/', include('core.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
