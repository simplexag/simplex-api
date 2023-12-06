from rest_framework import serializers
from .models import AccountProducts
from django_restql.mixins import DynamicFieldsMixin
import uuid

class AccountProductsListSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = AccountProducts
        fields = ('__all__')

class AccountProductsDetailSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = AccountProducts
        fields = ('account','id','display_name','full_name','state','application_unit','bulk_unit','density','density_unit','bulk_density','bulk_density_unit','product_elements')
  
