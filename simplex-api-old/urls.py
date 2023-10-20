from django.urls import path, include

from simplex_api.views import not_found, app_error

handler404 = not_found
handler500 = app_error

urlpatterns = [
    path('api/messages/', include('messages_api.urls')),
]
