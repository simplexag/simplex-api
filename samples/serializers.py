from rest_framework import serializers
from .models import SampleEvent, SoilSampleDepthList, SamplesSoil, SampleSoilDepth, SoilExtraction, SampleSoilResults
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

class SoilExtractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilExtraction
        fields = ['id','display_name','full_name','units']

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

class SampleSoilResultsSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    #def __init__(self, *args, **kwargs):
    #    many = kwargs.pop('many', True)
    
    class Meta:
        model = SampleSoilResults
        fields = ['id','depth','extraction','value','unit','value_description'] 

class SampleEventSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    class Meta:
        model = SampleEvent
        fields = ('id','account','organization','field','name','date','type','number_samples','depths','has_results','has_rx','samples_soil')

class SamplesSoilSampleSoilDepthSampleSoilResultsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleSoilResults
        fields = ('id','extraction','value','unit','value_description')

class SamplesSoilSampleSoilDepthDetailSerializer(serializers.ModelSerializer):
    soil_results = SamplesSoilSampleSoilDepthSampleSoilResultsDetailSerializer(many=True, read_only=True)
    class Meta:
        model = SampleSoilDepth
        fields = ('id','sample_depth','soil_results')

class SamplesSoilDetailSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    depths = SamplesSoilSampleSoilDepthDetailSerializer(many=True, read_only=True)
    class Meta:
        model = SamplesSoil
        fields = ('id','label','geom','depths',) #,'soil_samples_depths'

class SampleEventSoilDetailSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    samples_soil = SamplesSoilDetailSerializer(many=True, read_only=True)
    class Meta:
        model = SampleEvent
        fields = ('id','account','organization','field','name','date','type','number_samples','depths','has_results','has_rx','samples_soil',)