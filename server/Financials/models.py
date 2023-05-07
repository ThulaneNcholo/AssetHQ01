from django.db import models
from owners.models import OwnerModel
from managers.models import ManagerModel
from applications.models import ApplicationModel
from Vendors.models import VendorModel
from property.models import PropertyModel

# Create your models here.
class ExpenseModel(models.Model):
    property = models.ForeignKey(PropertyModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='property_expense')
    tenant = models.ForeignKey(ApplicationModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='tenant_expense')
    vendor = models.ForeignKey(VendorModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='vendor_expense')
    name = models.CharField(max_length=100,null=True,blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class IncomeModel(models.Model):
    property = models.ForeignKey(PropertyModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='property_income')
    tenant = models.ForeignKey(ApplicationModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='tenant_income')
    vendor = models.ForeignKey(VendorModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='vendor_income')
    name = models.CharField(max_length=100,null=True,blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True)
    date = models.DateField(blank=True,null=True)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class RentModel(models.Model):
    property = models.ForeignKey(PropertyModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='property_rent')
    tenant = models.ForeignKey(ApplicationModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='tenant_rent')
    amount = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


