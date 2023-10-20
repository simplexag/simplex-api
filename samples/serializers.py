from rest_framework import serializers
from .models import SampleEvent
from django_restql.mixins import DynamicFieldsMixin
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class SampleEventSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = SampleEvent
        fields = ('__all__')
