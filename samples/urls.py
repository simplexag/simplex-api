from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import SampleEventViewSet, SoilSampleDepthListViewSet, SamplesSoilSerializerListViewSet, SoilExtractionViewSet, SampleSoilResultsSerializerViewSet, SampleEventSoilDetailSerializerViewSet

router = DefaultRouter()
router.register(r'account/(?P<account>[A-Za-z0-9_-]+)/sampleEvents', SampleEventViewSet, basename='Core')
router.register(r'account/(?P<account>[A-Za-z0-9_-]+)/sampleEvents/details', SampleEventSoilDetailSerializerViewSet, basename='Core')
router.register(r'SoilSampleDepths', SoilSampleDepthListViewSet, basename='Core')
router.register(r'SoilExtractions', SoilExtractionViewSet, basename='Core')
router.register(r'account/(?P<account>[A-Za-z0-9_-]+)/sampleEvents/(?P<event>[A-Za-z0-9_-]+)/samples', SamplesSoilSerializerListViewSet, basename='Core')
router.register(r'account/(?P<account>[A-Za-z0-9_-]+)/sampleEvents/(?P<event>[A-Za-z0-9_-]+)/samples/soil/results', SampleSoilResultsSerializerViewSet, basename='Core')

#router.register(r'account/(?P<account>[A-Za-z0-9_-]+)/farmBoundaries', FarmLocationList, basename='Core')
urlpatterns = [
    path('', include(router.urls)),
]