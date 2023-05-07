from django.db import models
from owners.models import OwnerModel
from managers.models import ManagerModel
from applications.models import ApplicationModel

# Create your models here.
class PropertyForModel(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class PropertyTypeModel(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class EletricityModel(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class PropertyFeatures(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class AvailabilityModel(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    available_date = models.DateField(auto_now_add=False,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

# Delete this model changed to leaseMode   
class PropertyTenant(models.Model):
    applicant = models.ForeignKey(ApplicationModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='property_tenant')
    move_in = models.DateField(auto_now=False)
    move_out = models.DateField(auto_now=False)
    fee = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    paydate = models.CharField(max_length=200,null=True,blank=True)
    status = models.CharField(max_length=200,null=True,blank=True,default='Tenant')
    applicationstatus = models.CharField(max_length=200,null=True,blank=True,default='Approved')
    updated_at = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.applicant.first_name
    




class PropertyModel(models.Model):
    listing_number = models.CharField(max_length=200,null=True,blank=True)
    propertyName = models.CharField(max_length=200,null=True,blank=True)
    street = models.CharField(max_length=200,null=True,blank=True)
    town = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    postal_code = models.CharField(max_length=200,null=True,blank=True)
    province = models.CharField(max_length=200,null=True,blank=True)
    property_for = models.ForeignKey(PropertyForModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='property_is_for')
    property_type = models.ForeignKey(PropertyTypeModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='property_type')
    features_property = models.ManyToManyField(PropertyFeatures,blank=True,default=None , related_name='propertyfeatures')
    availability = models.ForeignKey(AvailabilityModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='property_availability')
    bedrooms = models.DecimalField(max_digits=10, decimal_places=1)
    bathrooms = models.DecimalField(max_digits=10, decimal_places=1)
    garage = models.CharField(max_length=200,null=True,blank=True)
    Floor_Size = models.DecimalField(max_digits=10, decimal_places=2)
    Erf_Size = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.TextField(blank = True)
    Furnished = models.CharField(max_length=200,null=True,blank=True)
    eletricity_type = models.ForeignKey(EletricityModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='eletricity_type')
    owners = models.ManyToManyField(OwnerModel,blank=True,default=None , related_name='property_owner')
    managers = models.ManyToManyField(ManagerModel,blank=True,default=None , related_name='property_managers')
    property_applications = models.ManyToManyField(ApplicationModel,blank=True,default=None , related_name='property_applicants')
    tenants = models.ManyToManyField(PropertyTenant,blank=True,default=None , related_name='listing_tenants')
    property_tenant = models.ForeignKey(ApplicationModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='moved_in_tenant')
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    status = models.CharField(max_length=200,null=True,blank=True,default='Active')
    coverImage = models.ImageField(null=True, blank=True,upload_to='static/images')
    image1 = models.ImageField(null=True, blank=True,upload_to='static/images')
    image2 = models.ImageField(null=True, blank=True,upload_to='static/images')
    image3 = models.ImageField(null=True, blank=True,upload_to='static/images')
    updated_at = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.listing_number
    

class PropertyViewings(models.Model):
    property = models.ForeignKey(PropertyModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='Showing_Property')
    viewing_date = models.DateField(auto_now=False)
    viewing_time = models.CharField(max_length=200,null=True,blank=True)
    client = models.CharField(max_length=200,null=True,blank=True)
    contact = models.CharField(max_length=200,null=True,blank=True)
    status = models.CharField(max_length=200,null=True,blank=True,default='Pending')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.status
    

class LeaseModel(models.Model):
    lease_number = models.CharField(max_length=200,null=True,blank=True)
    tenant = models.ForeignKey(ApplicationModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='Tenant')
    property = models.ForeignKey(PropertyModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='Property')
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    rent_amount = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    payment_schedule = models.CharField(max_length=200,null=True,blank=True)
    security_deposit = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    late_fee = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    late_payment_policiy = models.TextField(blank=True,null=True)
    utilities = models.TextField(blank=True,null=True)
    maintenance_responsibilities = models.TextField(blank=True,null=True)
    renewal_options = models.TextField(blank=True,null=True)
    subletting_policy = models.TextField(blank=True,null=True)
    pet_policy = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=200,null=True,blank=True,default='Tenant')
    application_status = models.CharField(max_length=200,null=True,blank=True,default='Approved')
    updated_at = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.lease_number