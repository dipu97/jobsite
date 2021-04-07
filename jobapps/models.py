from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class JobPost(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200,null=True,blank=True)
    job_description = models.TextField(null=True,blank=True)
    job_requirements = models.TextField(null=True,blank=True)
    responsibilities = models.TextField(null=True,blank=True)
    exprience = models.CharField(max_length=10,null=True,blank=True)
    salary = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    benefits = models.TextField(null=True,blank=True)
    job_nature = models.CharField(max_length=200,null=True,blank=True)
    is_published=models.BooleanField(default=False)