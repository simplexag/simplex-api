import uuid
from django.db import models
from softdelete.models import SoftDeleteObject
from core.models import Account, Organization

# Create your models here.
###### Soil Recomnndation Elements Reference Tables
class StandardSoilRxElements(SoftDeleteObject, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    display_name = models.CharField(max_length=20,blank=False,null=False)
    full_name = models.CharField(max_length=50,blank=False,null=False)
    order = models.IntegerField()
    default_min_rate = models.FloatField(blank=True, null=True)
    default_max_rate = models.FloatField(blank=True, null=True)
    default_switch_rate = models.FloatField(blank=True, null=True)
    default_rate_unit = models.CharField(max_length=20,blank=False,null=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return str(self.display_name)

class StandardRxCrops(SoftDeleteObject, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    display_name = models.CharField(max_length=50,blank=False,null=False)
    full_name = models.CharField(max_length=50,blank=False,null=False)

    def __str__(self):
        return str(self.display_name)

class EquationSets(SoftDeleteObject, models.Model):
    class EquationTypes(models.TextChoices):
        SOIL = 'S', 'Soil'
        TISSUE = 'T', 'Tissue'
        NEMATODE = 'N', 'Nematode'
    
    class EquationSource(models.TextChoices):
        USER = 'U', 'User'
        UNIVERSITY = 'V', 'University'
        LAB = 'L', 'Lab'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False, null=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=20,blank=False,null=False)
    type = models.CharField(max_length=1, choices=EquationTypes.choices, default=EquationTypes.SOIL,blank=False,null=False)
    source = models.CharField(max_length=1, choices=EquationSource.choices, default=EquationSource.USER,blank=False,null=False)

    class Meta:
        ordering = ['name']
     
    def __str__(self):
        return str(self.name)
    
class EquationCrops(SoftDeleteObject, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    crop = models.ForeignKey(StandardRxCrops, on_delete=models.CASCADE,  related_name='equation_crop_ref')
    set = models.ForeignKey(EquationSets, on_delete=models.CASCADE,  related_name='equation_crops')

    class Meta:
        ordering = ['crop__display_name']

    def __str__(self):
        return str(self.crop.display_name)


# Model to store the equation for a crop and element
# code has the js code to run
# input hase the def of what the function params are
"""
input = {
    params: [
        {
        param:""
        source:"" # soil_result, user
        type:"" # number, text, option
        defult:0,
        soil_result_options: {
            extraction:""
            expected_unit:""
            },
        user_options: {
            display_name:"",
            unit:"",
            options:[]
            }
        }
    ]
}
"""
class EquationElement(SoftDeleteObject, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    element = models.ForeignKey(StandardSoilRxElements, on_delete=models.CASCADE,  related_name='equation_element_ref')
    crop = models.ForeignKey(EquationCrops, on_delete=models.CASCADE,  related_name='equation_elements')
    inputs = models.JSONField(blank=True,null=True)
    code = models.TextField(blank=True,null=True)
    output_unit = models.CharField(max_length=20,blank=True,null=True)

    class Meta:
        ordering = ['element__order']

    def __str__(self):
        return str(self.element.display_name)