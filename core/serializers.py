from rest_framework import serializers
from .models import Account, Organization, Grower, Farm, Field
from django_restql.mixins import DynamicFieldsMixin
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('__all__')

class OrganizationSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('__all__')

class GrowerSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Grower
        fields = ('__all__')

class FarmSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ('__all__')

class FieldSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ('__all__')
    """
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {representation['id']: representation}
    """
class FieldLocationSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        model = Field
        geo_field = "geom"

        # you can also explicitly declare which fields you want to include
        # as with a ModelSerializer.
        fields = ('id', 'name',)