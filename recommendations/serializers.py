from rest_framework import serializers
from .models import RxEvent
from django_restql.mixins import DynamicFieldsMixin
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class RxEventListSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = RxEvent
        fields = ('__all__')