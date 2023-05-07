from django.contrib import admin
from .models import ApplicationModel

# Register your models here.

class ApplicationsAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name','date_created'
    )

admin.site.register(ApplicationModel,ApplicationsAdmin) 
