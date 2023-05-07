from django.contrib import admin
from .models import *

# Register your models here.

class PropertyDocumentsAdmin(admin.ModelAdmin):
    list_display = (
        'name' , 'date_created'
    )

admin.site.register(PropertyDocument,PropertyDocumentsAdmin)
