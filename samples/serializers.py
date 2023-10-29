from rest_framework import serializers
from .models import SampleEvent, SoilSampleDepthList, SamplesSoil, SampleSoilDepth
from django_restql.mixins import DynamicFieldsMixin
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class SoilSampleDepthListSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = SoilSampleDepthList
        fields = ('id','name','start_depth','end_depth','column_depth')

#Serializer for the sample depths under a sample
class SampleSoilDepthListSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = SampleSoilDepth
        fields = ('id','sample','sample_depth') 

class SamplesSoilSampleSoilDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleSoilDepth
        fields = ['id','sample_depth']

class SamplesSoilSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    depths = SamplesSoilSampleSoilDepthSerializer(many=True)
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(SamplesSoilSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = SamplesSoil
        fields = ('id','sample_event','label','geom','depths')

    def create(self, validated_data):
        children = validated_data.pop('depths')
        parent = super().create(validated_data)
        for child in children: 
            child['sample'] = parent
        self.fields['depths'].create(children)
        return parent
    
class SampleEventSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    class Meta:
        model = SampleEvent
        fields = ('id','account','organization','field','name','date','type','number_samples','depths','has_results','has_rx','samples_soil')