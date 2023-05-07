from django.contrib import admin
from .models import *

# Register your models here.

# Status Register 
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = (
        'name','date_created'
    )

admin.site.register(TaskStatusModel,TaskStatusAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'task_number','date_created'
    )

admin.site.register(TaskModel,TaskAdmin)