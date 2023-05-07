from django.contrib import admin
from .models import *

# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'name','date_created'
    )

admin.site.register(ExpenseModel,ExpenseAdmin)

class IncomeAdmin(admin.ModelAdmin):
    list_display = (
        'name','date_created'
    )

admin.site.register(IncomeModel,IncomeAdmin)

class RentAdmin(admin.ModelAdmin):
    list_display = (
        'name','date_created'
    )

admin.site.register(RentModel,RentAdmin)
