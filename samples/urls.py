from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import SampleEventViewSet

router = DefaultRouter()
router.register(r'account/(?P<account>[A-Za-z0-9_-]+)/sampleEvents', SampleEventViewSet, basename='Core')
#router.register(r'account/(?P<account>[A-Za-z0-9_-]+)/farmBoundaries', FarmLocationList, basename='Core')
urlpatterns = [
    path('', include(router.urls)),
]