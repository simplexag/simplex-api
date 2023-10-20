import uuid
from django.db import models
from django_softdelete.models import SoftDeleteModel
from django.db.models import Q
from django.contrib.gis.db import models
from core.models import Account, Organization, Field
from datetime import date
from django.contrib.postgres.fields import ArrayField


#All depth is stored in cm, these are combinations of depths a sample can be part of 
class SoilSampleDepthList(SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100,blank=False,null=False)
    start_depth = models.FloatField(blank=True,null=True)
    end_depth = models.FloatField(blank=True,null=True)
    column_depth = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.name

#Holds all aample event types
class SampleEvent(SoftDeleteModel):
    #Enum for the different 
    class SampleTypes(models.TextChoices):
        SOIL = 'S', 'Soil'
        TISSUE = 'T', 'Tissue'
        NEMATODE = 'N', 'Nematode'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False, null=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=False, null=False)
    field = models.ForeignKey(Field, on_delete=models.CASCADE,blank=False,null=False)
    name = models.CharField(max_length=100,blank=False,null=False)
    date = models.DateField(default=date.today)
    type = models.CharField(max_length=1, choices=SampleTypes.choices, default=SampleTypes.SOIL,blank=False,null=False)
    number_samples = models.IntegerField(default=0)
    depths = models.ManyToManyField(SoilSampleDepthList,related_name="sample_event_depths")
    has_results = models.BooleanField(default=False)
    has_rx = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

#Model for individual soil samples
class SamplesSoil(SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sample_event = models.ForeignKey(SampleEvent, on_delete=models.CASCADE)
    sample_depth = models.ForeignKey(SoilSampleDepthList, on_delete=models.CASCADE)
    label = models.CharField(max_length=25,blank=False,null=False)
    geom = models.GeometryField(blank=True,null=True, srid=4326)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
