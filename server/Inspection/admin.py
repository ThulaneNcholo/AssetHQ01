from django.contrib import admin
from .models import InspectionModel,RoomModel,ItemModel,PhotoModel

# Register your models here.
admin.site.register(InspectionModel)
admin.site.register(RoomModel)
admin.site.register(ItemModel)
admin.site.register(PhotoModel)