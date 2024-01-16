from django.db import models
import uuid
from core.models import Account, Organization, Field
from equations.models import EquationSets, EquationCrops, StandardSoilRxElements, StandardRxCrops
from samples.models import SampleEvent

#Holds all sample event types
class RxEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False, null=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=100,blank=False,null=False)
    field = models.ForeignKey(Field, on_delete=models.CASCADE,blank=False,null=False)
    sample_event = models.ForeignKey(SampleEvent, on_delete=models.PROTECT,blank=False,null=False)
    equation_set = models.ForeignKey(EquationSets, on_delete=models.PROTECT,blank=False,null=False)
    equation_crop = models.ForeignKey(StandardRxCrops, on_delete=models.PROTECT,blank=False,null=False)
    equation_elements = models.ManyToManyField(StandardSoilRxElements)
    equation_detials = models.JSONField(blank=False,null=False)
    stats = models.JSONField(blank=False,null=False)
    geojson = models.FileField(upload_to='rx/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name