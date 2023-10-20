from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, OrganizationViewSet, GrowerViewSet, FarmViewSet, FieldViewSet, FarmLocationList

router = DefaultRouter()
router.register(r'user_account', AccountViewSet, basename='Core')
router.register(r'account/(?P<account>[A-Za-z0-9_-]+)/organizations', OrganizationViewSet, basename='Core')
router.register(r'account/(?P<account>[A-Za-z0-9_-]+)/growers', GrowerViewSet, basename='Core')
router.register(r'account/(?P<account>[A-Za-z0-9_-]+)/farms', FarmViewSet, basename='Core')
router.register(r'account/(?P<account>[A-Za-z0-9_-]+)/fields', FieldViewSet, basename='Core')
#router.register(r'account/(?P<account>[A-Za-z0-9_-]+)/farmBoundaries', FarmLocationList, basename='Core')
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'account/(?P<account>[A-Za-z0-9_-]+)/farmBoundaries', FarmLocationList.as_view(), name="instances"),
]