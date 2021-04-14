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
    location=models.CharField(max_length=255,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    deadline=models.DateTimeField(auto_now_add=False)
    application_process=models.CharField(max_length=255,null=True,blank=True)
    skills=models.CharField(max_length=255,null=True,blank=True)
    type=models.CharField(max_length=255,null=True,blank=True)
    company_logo=models.ImageField(null=True,upload_to="photos/logo/%y/%m/%d")
    education=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title


class ApplyForJob(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    job_id = models.ForeignKey(JobPost,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField()
    address = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(null=True,upload_to="photos/logo/%y/%m/%d")
    resume = models.FileField(upload_to='resume/%y/%m/%d',blank=True)
    cover_letter = models.TextField()
    salary_exceptation = models.DecimalField(max_digits=15,null=True,blank=True,decimal_places=2)

    def __str__(self):
        return self.job_id.title