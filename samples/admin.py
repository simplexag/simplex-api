from django.contrib import admin
from .models import SoilSampleDepthList, SampleEvent, SamplesSoil, SampleSoilDepth
from core.models import Account, Field
# Register your models here.

class SoilSampleDepthListAdmin(admin.ModelAdmin):
    pass

admin.site.register(SoilSampleDepthList, SoilSampleDepthListAdmin)

class SampleEventListAdmin(admin.ModelAdmin):
    pass

admin.site.register(SampleEvent, SampleEventListAdmin)

class SamplesSoilAdmin(admin.ModelAdmin):
    pass

admin.site.register(SamplesSoil, SamplesSoilAdmin)

class SampleSoilDepthAdmin(admin.ModelAdmin):
    pass

admin.site.register(SampleSoilDepth, SampleSoilDepthAdmin)