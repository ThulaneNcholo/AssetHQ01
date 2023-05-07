from django.contrib import admin
from .models import OwnerModel,OwnerManagement

# Register your models here.

# Owner Model 
class OwnerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name','date_created'
    )

admin.site.register(OwnerModel,OwnerAdmin) 

# Management Model
class OwnerManagementAdmin(admin.ModelAdmin):
    list_display = (
        'owner', 'date_created'
    )

admin.site.register(OwnerManagement,OwnerManagementAdmin)