from django.contrib import admin
from .models import *
# Register your models here.

# Property is For 
class PropertyForAdmin(admin.ModelAdmin):
    list_display = (
        'name','date_created'
    )

admin.site.register(PropertyForModel,PropertyForAdmin)

# Property type 
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name','date_created'
    )

admin.site.register(PropertyTypeModel,PropertyTypeAdmin)

# Property type 
class eletricityAdmin(admin.ModelAdmin):
    list_display = (
        'name','date_created'
    )

admin.site.register(EletricityModel,eletricityAdmin)

# Property Features 
class featuresAdmin(admin.ModelAdmin):
    list_display = (
        'name','date_created'
    )

admin.site.register(PropertyFeatures,featuresAdmin)

# Property Availability 
class availabilityAdmin(admin.ModelAdmin):
    list_display = (
        'name','date_created'
    )

admin.site.register(AvailabilityModel,availabilityAdmin)

# Property 
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'listing_number','date_created'
    )

admin.site.register(PropertyModel,PropertyAdmin)

# Property 
class PropertyTenantadmin(admin.ModelAdmin):
    list_display = (
        'applicant','date_created'
    )

admin.site.register(PropertyTenant,PropertyTenantadmin)

# leaseModel 
class LeaseModelAdmin(admin.ModelAdmin):
    list_display = (
        'lease_number','date_created'
    )

admin.site.register(LeaseModel,LeaseModelAdmin)

# Viewings Model 
class ViewingsModelAdmin(admin.ModelAdmin):
    list_display = (
        'property','viewing_date','viewing_time'
    )

admin.site.register(PropertyViewings,ViewingsModelAdmin)