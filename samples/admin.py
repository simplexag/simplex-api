from django.contrib import admin
from .models import SoilSampleDepthList, SampleEvent, SamplesSoil, SampleSoilDepth, SoilElement, StandardSoilElements, SoilExtraction, StandardSoilExtractions, SampleSoilResults
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

class SoilElementAdmin(admin.ModelAdmin):
    pass

admin.site.register(SoilElement, SoilElementAdmin)

class StandardSoilElementsAdmin(admin.ModelAdmin):
    pass

admin.site.register(StandardSoilElements, StandardSoilElementsAdmin)

class SoilExtractionAdmin(admin.ModelAdmin):
    pass

admin.site.register(SoilExtraction, SoilExtractionAdmin)

class StandardSoilExtractionsAdmin(admin.ModelAdmin):
    pass

admin.site.register(StandardSoilExtractions, StandardSoilExtractionsAdmin)

class SampleSoilResultsAdmin(admin.ModelAdmin):
    pass

admin.site.register(SampleSoilResults, SampleSoilResultsAdmin)

