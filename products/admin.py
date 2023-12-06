from django.contrib import admin
from .models import AccountProducts
# Register your models here.

class AccountProductsAdmin(admin.ModelAdmin):
    pass

admin.site.register(AccountProducts,AccountProductsAdmin)