from django.db import models
from property.models import PropertyModel
from managers.models import ManagerModel
from owners.models import OwnerModel
from applications.models import ApplicationModel
from Vendors.models import VendorModel

# Create your models here.
class PropertyDocument(models.Model):
    property = models.ForeignKey(PropertyModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='Property_documents')
    file = models.FileField(null=True, blank=True,upload_to='static/Files')
    name = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    

