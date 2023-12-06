import uuid
from django.db import models
from softdelete.models import SoftDeleteObject
from core.models import Account, Organization
from equations.models import StandardSoilRxElements

class StandardProducts(SoftDeleteObject, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    display_name = models.CharField(max_length=20,blank=False,null=False)
    full_name = models.CharField(max_length=50,blank=False,null=False)

    class Meta:
        ordering = ['display_name']

    def __str__(self):
        return str(self.display_name)

class StandardProductElements(SoftDeleteObject, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(StandardProducts, on_delete=models.CASCADE, blank=False, null=False, related_name='std_product_element')
    element = models.ForeignKey(StandardSoilRxElements, on_delete=models.CASCADE, blank=False, null=False, related_name='std_rx_element')
    value = models.FloatField(blank=True, null=True)
    primary = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class AccountProducts(SoftDeleteObject, models.Model):

    class ProductStates(models.TextChoices):
        SOLID = 'S', 'Solid'
        LIQUID = 'L', 'Liquid'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False, null=False)
    display_name = models.CharField(max_length=20,blank=False,null=False)
    full_name = models.CharField(max_length=50,blank=False,null=False)
    state = models.CharField(max_length=1, choices=ProductStates.choices, default=ProductStates.SOLID,blank=False,null=False)
    application_unit = models.CharField(max_length=20,blank=False,null=False)
    bulk_unit = models.CharField(max_length=20,blank=False,null=False)
    density = models.FloatField(blank=True, null=True)
    density_unit = models.CharField(max_length=20,blank=True,null=True)
    bulk_density = models.FloatField(blank=True, null=True)
    bulk_density_unit = models.CharField(max_length=20,blank=True,null=True)
    product_elements = models.JSONField(blank=True,null=True)

    class Meta:
        ordering = ['display_name']

    def __str__(self):
        return str(self.display_name)




