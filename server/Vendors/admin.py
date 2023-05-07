from django.contrib import admin
from .models import VendorModel,VendorServices

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = (
        'vendor_id','company_name' ,'date_created'
    )

admin.site.register(VendorModel,VendorAdmin)

class VendorServicesAdmin(admin.ModelAdmin):
    list_display = (
        'name','date_created'
    )

admin.site.register(VendorServices,VendorServicesAdmin)