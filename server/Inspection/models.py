from django.db import models
from property.models import PropertyModel
from managers.models import ManagerModel
from owners.models import OwnerModel
from applications.models import ApplicationModel
from Vendors.models import VendorModel

# Create your models here.
class InspectionModel(models.Model):
    inspection_number = models.CharField(max_length=200,null=True,blank=True)
    property = models.ForeignKey(PropertyModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='Property_inspection')
    inspector = models.ForeignKey(ManagerModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='Inspector')
    applicant = models.ManyToManyField(ApplicationModel,blank=True,default=None , related_name='Applicant')
    owners = models.ManyToManyField(OwnerModel,blank=True,default=None , related_name='Owner')
    vendors = models.ManyToManyField(VendorModel,blank=True,default=None , related_name='Vendor')
    managers = models.ManyToManyField(ManagerModel,blank=True,default=None , related_name='Manager')
    date = models.DateField(auto_now_add=True)
    # remove this comments for file version 
    comments = models.TextField(blank = True)
    updated_at = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    

class RoomModel(models.Model):
    name = models.CharField(max_length=255)
    comments = models.TextField(blank = True)
    inspectionID = models.ManyToManyField(InspectionModel,blank=True,default=None , related_name='Inspection_id')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    
    

class ItemModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    room = models.ForeignKey(RoomModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='Room')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    
    

class PhotoModel(models.Model):
    image1 = models.ImageField(null=True, blank=True,upload_to='static/images')
    image2 = models.ImageField(null=True, blank=True,upload_to='static/images')
    image3 = models.ImageField(null=True, blank=True,upload_to='static/images')
    item = models.ForeignKey(ItemModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='Item')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    