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

###### Soil Extraction Reference Tables
class StandardSoilElements(SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=50,blank=False,null=False)

class StandardSoilExtractions(SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=50,blank=False,null=False)

class SoilElement(SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    display_name = models.CharField(max_length=20,blank=False,null=False)
    full_name = models.CharField(max_length=20,blank=False,null=False)
    std_related = models.ManyToManyField(StandardSoilElements,related_name="std_soil_elements",blank=True,null=True)

class SoilExtraction(SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    display_name = models.CharField(max_length=20,blank=False,null=False)
    full_name = models.CharField(max_length=20,blank=False,null=False)
    std_related = models.ManyToManyField(StandardSoilExtractions,related_name="std_soil_extractions",blank=True,null=True)
###### End Soil Extraction Reference Tables

#Holds all sample event types
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
    depths = models.ManyToManyField(SoilSampleDepthList,related_name="sample_event_depths",blank=True,null=True)
    has_results = models.BooleanField(default=False)
    has_rx = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.field.farm.grower,self.field.farm,self.field,self.name

#Model for individual soil samples
class SamplesSoil(SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sample_event = models.ForeignKey(SampleEvent, on_delete=models.CASCADE,  related_name='samples_soil')
    label = models.CharField(max_length=25,blank=False,null=False)
    geom = models.GeometryField(blank=True,null=True, srid=4326)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sample_event.name

#Model for each depth of a soil samples
class SampleSoilDepth(SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sample = models.ForeignKey(SamplesSoil, on_delete=models.CASCADE, related_name='depths')
    sample_depth = models.ForeignKey(SoilSampleDepthList, on_delete=models.CASCADE)

    def __str__(self):
        return self.sample.sample_event.name, self.sample_depth.name

#Model for each lab result of a soil samples at a depth
class SampleSoilResults(SoftDeleteModel):
    #Enum for the different Value discriptions
    class ValueDescriptions(models.TextChoices):
        VL = 'VL', 'Very Low'
        L = 'L', 'Low'
        M = 'M', 'Medium'
        H = 'H', 'High'
        VH = 'VH', 'Very High'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    depth = models.ForeignKey(SampleSoilDepth, on_delete=models.CASCADE, blank=False, null=False)
    element = models.ForeignKey(SoilElement, on_delete=models.CASCADE ,blank=False, null=False)
    extraction = models.ForeignKey(SoilExtraction, on_delete=models.CASCADE, blank=False, null=False)
    value = models.FloatField(blank=False,null=False)
    unit = models.CharField(max_length=20,blank=False,null=False)
    value_description = models.CharField(max_length=2, choices=ValueDescriptions.choices, default=ValueDescriptions.VL,blank=True,null=True)