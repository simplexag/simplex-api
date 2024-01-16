from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import RxListViewSet

router = DefaultRouter()
router.register(r'(?P<account>[A-Za-z0-9_-]+)/rxEvents', RxListViewSet, basename='Core')

#router.register(r'account/(?P<account>[A-Za-z0-9_-]+)/farmBoundaries', FarmLocationList, basename='Core')
urlpatterns = [
    path('', include(router.urls)),
]