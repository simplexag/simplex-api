from rest_framework import serializers
from .models import SampleEvent, SoilSampleDepthList
from django_restql.mixins import DynamicFieldsMixin
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class SampleEventSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = SampleEvent
        fields = ('__all__')

class SoilSampleDepthListSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = SoilSampleDepthList
        fields = ('id','name','start_depth','end_depth','column_depth')