from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.expressions import F
# Create your models here.


class User(AbstractUser):
    is_job_seekers = models.BooleanField(default=False)
    is_employeers = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

class JobSeekers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=250,blank=True,null=True)
    nid = models.CharField(max_length=20,blank=True,null=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    area_of_interest = models.CharField(null=True,blank=True,max_length=250)
    resume = models.FileField(upload_to='resume/%y/%m/%d',blank=True)
    phone = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Employeers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=30,null=True,blank=True)
    address = models.CharField(max_length=250,blank=True,null=True)
    company_description = models.TextField(null=True,blank=True)
    company_type = models.CharField(max_length=250,blank=True,null=True)
    website_url = models.CharField(max_length=250,blank=True,null=True)
    contact = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
