from django.contrib import admin
from .models import ManagerModel

# Register your models here.
class ManagerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name','date_created'
    )

admin.site.register(ManagerModel,ManagerAdmin)
