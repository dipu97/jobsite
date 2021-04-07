from django.contrib import admin
from jobapps.models import *
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(JobSeekers)
admin.site.register(Employeers)

