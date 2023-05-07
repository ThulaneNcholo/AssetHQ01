from django.db import models
from accounts.models import UserModel

# Create your models here.
class ManagerModel(models.Model):
    user = models.ForeignKey(UserModel,null=True, on_delete=models.CASCADE,blank=True,default=None , related_name='user_manager')
    manager_number = models.CharField(max_length=200,null=True,blank=True)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    street = models.CharField(max_length=200,null=True,blank=True)
    town = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    postal_code = models.CharField(max_length=200,null=True,blank=True)
    province = models.CharField(max_length=200,null=True,blank=True)
    role = models.CharField(max_length=200,null=True,blank=True,default='manager')
    active = models.CharField(max_length=200,null=True,blank=True,default='active')
    profile_pic = models.ImageField(null=True, blank=True,upload_to='static/images')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name