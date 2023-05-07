from django.db import models
from property.models import PropertyModel
from managers.models import ManagerModel
from owners.models import OwnerModel
from applications.models import ApplicationModel
from Vendors.models import VendorModel

# Create your models here.
class TaskStatusModel(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class TaskModel(models.Model):
    task_number = models.CharField(max_length=200,null=True,blank=True)
    property = models.ForeignKey(PropertyModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='Task_Property')
    owners = models.ManyToManyField(OwnerModel,blank=True,default=None , related_name='Task_owner')
    managers = models.ManyToManyField(ManagerModel,blank=True,default=None , related_name='Task_managers')
    created_by = models.ForeignKey(ManagerModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='created_byTask')
    asssigned_vendor = models.ManyToManyField(VendorModel,blank=True,default=None , related_name='Task_vendors')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(TaskStatusModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='Task_status')
    due_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.task_number