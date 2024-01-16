from django.contrib import admin
from .models import RxEvent
# Register your models here.

class RxEventListAdmin(admin.ModelAdmin):
    pass

admin.site.register(RxEvent, RxEventListAdmin)

