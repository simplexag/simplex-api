from django.contrib import admin
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Account, Organization, Grower, Farm, Field
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(Account, AccountAdmin)

class OrganizationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Organization, OrganizationAdmin)

class GrowerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Grower, GrowerAdmin)

class FarmAdmin(admin.ModelAdmin):
    pass

admin.site.register(Farm, FarmAdmin)

class FieldAdmin(admin.GeoModelAdmin):
    pass

admin.site.register(Field, FieldAdmin)