from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import EquationSetsSerializerViewSet, EquationElementDetailViewSet, StandardSoilRxElementsViewSet, StandardRxCropsViewSet, EquationSetsViewSet, EquationCropsViewSet, EquationElementViewSet

router = DefaultRouter()
router.register(r'(?P<account>[A-Za-z0-9_-]+)/equationSetsFull', EquationSetsSerializerViewSet, basename='Core')
#router.register(r'equationElement', EquationElementDetailViewSet, basename='Core')
router.register(r'equationStandardSoilRxElements', StandardSoilRxElementsViewSet, basename='Core')
router.register(r'equationStandardRxCrops', StandardRxCropsViewSet, basename='Core')
router.register(r'(?P<account>[A-Za-z0-9_-]+)/equationSets', EquationSetsViewSet, basename='Core')
router.register(r'(?P<set>[A-Za-z0-9_-]+)/equationCrops', EquationCropsViewSet, basename='Core')
router.register(r'(?P<crop>[A-Za-z0-9_-]+)/equationElements', EquationElementViewSet, basename='Core')
router.register(r'equationElement', EquationElementDetailViewSet, basename='Core')
#router.register(r'equationStandardSoilRxElements', StandardSoilRxElementsViewSet, basename='Core')
#router.register(r'equationStandardRxCrops', StandardRxCropsViewSet, basename='Core')

urlpatterns = [
    path('', include(router.urls)),
]