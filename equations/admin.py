from django.contrib import admin
from .models import StandardSoilRxElements, StandardRxCrops, EquationSets, EquationCrops, EquationElement
# Register your models here.

class StandardSoilRxElementsAdmin(admin.ModelAdmin):
    pass

admin.site.register(StandardSoilRxElements,StandardSoilRxElementsAdmin)

class StandardRxCropsAdmin(admin.ModelAdmin):
    pass

admin.site.register(StandardRxCrops,StandardRxCropsAdmin)

class EquationSetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'account','organization')
    pass

admin.site.register(EquationSets,EquationSetsAdmin)

class EquationCropsAdmin(admin.ModelAdmin):
    list_display = ('crop', 'set')
    pass

admin.site.register(EquationCrops,EquationCropsAdmin)

class EquationElementAdmin(admin.ModelAdmin):
    list_display = ('element', 'crop')
    pass

admin.site.register(EquationElement,EquationElementAdmin)