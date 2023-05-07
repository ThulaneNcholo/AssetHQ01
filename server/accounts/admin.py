from django.contrib import admin
from .models import UserModel

# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'first_name','last_name','email','date_created'
    )

admin.site.register(UserModel,UserModelAdmin)