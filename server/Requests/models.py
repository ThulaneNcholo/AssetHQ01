from django.db import models
from property.models import PropertyModel
from managers.models import ManagerModel
from owners.models import OwnerModel
from applications.models import ApplicationModel
from Vendors.models import VendorModel

# Create your models here.
class PriorityModel(models  .Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class MaintenanceStatusModel(models  .Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class MaintenanceRequest(models.Model):
    property = models.ForeignKey(PropertyModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='Property_maintenance')
    tenant = models.ForeignKey(ApplicationModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='maintenance_tenant')
    assigned_manager = models.ForeignKey(ManagerModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='maintenance_manager')
    owners = models.ManyToManyField(OwnerModel,blank=True,default=None , related_name='maintenance_owner')
    vendor = models.ForeignKey(VendorModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='maintenance_vendor')
    title =  models.CharField(max_length=255)
    description = models.TextField(blank = True)
    image = models.ImageField(null=True, blank=True,upload_to='static/images')
    status = models.ForeignKey(MaintenanceStatusModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='maintenance_status')
    priority = models.ForeignKey(PriorityModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='maintenance_priority')
    date_completed = models.DateTimeField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
     
