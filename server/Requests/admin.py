from django.contrib import admin
from .models import *

# Register your models here.
class MaintenanceStatusAdmin(admin.ModelAdmin):
    list_display = (
        'name' , 'date_created'
    )

admin.site.register(MaintenanceStatusModel,MaintenanceStatusAdmin)

class PriorityAdmin(admin.ModelAdmin):
    list_display = (
        'name' , 'date_created'
    )

admin.site.register(PriorityModel,PriorityAdmin)

class MaintenanceAdmin(admin.ModelAdmin):
    list_display = (
        'title' , 'date_created'
    )

admin.site.register(MaintenanceRequest,MaintenanceAdmin)

