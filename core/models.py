import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from softdelete.models import SoftDeleteObject
from django.db.models import Q
from django.contrib.gis.db import models

class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=200,blank=True,null=True)
    address_2 = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=50,blank=True,null=True)
    zipcode = models.CharField(max_length=50,blank=True,null=True)
    country = models.CharField(max_length=50, default='US')
    phone_number = PhoneNumberField(blank=True,null=True)
    owner = models.CharField(max_length=100,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class AccoutUsers(models.Model):
    user = models.CharField(max_length=100,db_index=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

class Organization(SoftDeleteObject):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

class Grower(SoftDeleteObject):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=200,blank=True,null=True)
    address_2 = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=50,blank=True,null=True)
    zipcode = models.CharField(max_length=50,blank=True,null=True)
    country = models.CharField(max_length=50, default='US')
    phone_number = PhoneNumberField(blank=True,null=True)
    area = models.FloatField(default=0.0)
    marker = models.PointField(blank=True,null=True, srid=4326)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    """
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['organization', 'name'],
                condition=Q(is_deleted=False),
                name='grower_unique_if_not_deleted')
        ]
    """

    def __str__(self):
        return self.name
    
    
class Farm(SoftDeleteObject):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    grower = models.ForeignKey(Grower, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    area = models.FloatField(default=0.0)
    marker = models.PointField(blank=True,null=True, srid=4326)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    """
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['grower', 'name'],
                condition=Q(is_deleted=False),
                name='farm_unique_if_not_deleted')
        ]
    """
    def __str__(self):
        return self.name
    

class Field(SoftDeleteObject):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    area = models.FloatField(default=0.0)
    marker = models.PointField(blank=True,null=True, srid=4326)
    geom = models.GeometryField(blank=True,null=True, srid=4326)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    """
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['farm', 'name'],
                condition=Q(is_deleted=False),
                name='field_unique_if_not_deleted')
        ]
    """

    def __str__(self):
        return self.name