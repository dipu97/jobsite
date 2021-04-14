from django.shortcuts import render
from jobapps.model_choices import *
# Create your views here.
def index(request):
    context={
        'Category': Category,
    }
    return render(request,'pages/index.html',context)

def job_details(request):
    return render(request,'jobs/job_details.html')
def register(request):
    return render(request,'accounts/register.html')

def login(request):
    return render(request,'accounts/login.html')