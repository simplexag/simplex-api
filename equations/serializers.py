from rest_framework import serializers
from .models import EquationSets, EquationCrops, EquationElement, StandardSoilRxElements, StandardRxCrops
from django_restql.mixins import DynamicFieldsMixin

class StandardSoilRxElementsSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = StandardSoilRxElements
        fields = ('id','display_name','full_name','order')

class StandardRxCropsSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = StandardRxCrops
        fields = ('id','display_name','full_name')

class EquationElementOnlySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = EquationElement
        fields = ('id','element','crop')

class EquationElementSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = EquationElement
        fields = ('id','element')

##Used to edit the crops in an equation set when not coming throguht set Serializer
##for some reason, cane not get them to work toghter so madd a differnet one
class EquationCropsOnlySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    equation_elements = EquationElementSerializer(many=True)

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(EquationCropsOnlySerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = EquationCrops
        fields = ('id','crop','equation_elements','set')

    def create(self, validated_data):
        children = validated_data.pop('equation_elements')
        parent = super().create(validated_data)
        print (parent)
        for child in children: 
            child['crop'] = parent
        self.fields['equation_elements'].create(children)
        return parent

class EquationCropsSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    equation_elements = EquationElementSerializer(many=True)

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(EquationCropsSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = EquationCrops
        fields = ('id','crop','equation_elements')

    def create(self, validated_data):
        children = validated_data.pop('equation_elements')
        parent = super().create(validated_data)
        print (parent)
        for child in children: 
            child['crop'] = parent
        self.fields['equation_elements'].create(children)
        return parent

class EquationSetsSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    equation_crops = EquationCropsSerializer(many=True)

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(EquationSetsSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = EquationSets
        fields = ('id','account','organization','name','type','source','equation_crops')
    
    def create(self, validated_data):
        children = validated_data.pop('equation_crops')
        parent = super().create(validated_data)
        for child in children: 
            child['set'] = parent
        self.fields['equation_crops'].create(children)
        return parent

#Serializers for getting the equation tree at once
class EquationElementListSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    element_name = serializers.CharField(source='element.display_name')
    class Meta:
        model = EquationElement
        fields = ('id','element_name')

class EquationCropsListSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    equation_elements = EquationElementListSerializer(many=True, read_only=True)
    crop_name = serializers.CharField(source='crop.display_name')
    class Meta:
        model = EquationCrops
        fields = ('id','crop_name','equation_elements')

class EquationSetsListSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    equation_crops = EquationCropsListSerializer(many=True, read_only=True)
    class Meta:
        model = EquationSets
        fields = ('id','name','type','source','equation_crops')

class EquationElementDetailSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    element_name = serializers.CharField(source='element.display_name')
    crop_name = serializers.CharField(source='crop.crop.display_name')
    set_name = serializers.CharField(source='crop.set.name')
    set_type = serializers.CharField(source='crop.set.type')
    set_source = serializers.CharField(source='crop.set.source')
    class Meta:
        model = EquationElement
        fields = ('id','element_name','crop_name','set_name','set_type','set_source','inputs','code','output_unit')