from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import AccountProductsListSerializerViewSet, AccountProductsDetailSerializer, AccountProductsDefaultsSerializerViewSet

router = DefaultRouter()
router.register(r'(?P<account>[A-Za-z0-9_-]+)/products', AccountProductsListSerializerViewSet, basename='Core')
router.register(r'(?P<account>[A-Za-z0-9_-]+)/productDetail', AccountProductsDetailSerializer, basename='Core')
router.register(r'(?P<account>[A-Za-z0-9_-]+)/productsDefaults', AccountProductsDefaultsSerializerViewSet, basename='Core')

urlpatterns = [
    path('', include(router.urls)),
]