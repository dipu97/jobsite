from django.contrib import admin
from .models import JobPost
from jobapps.models import *
# Register your models here.
admin.site.register(JobPost)
admin.site.register(ApplyForJob)