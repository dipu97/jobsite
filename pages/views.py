from django.shortcuts import render
from jobapps.model_choices import *
from jobapps.models import JobPost
from accounts.models import *
# Create your views here.
def index(request):
    latest=JobPost.objects.filter(is_published=True).order_by('-created_at')[:4]
    context={
        'Category': Category,
        'latest':latest,
    }
    return render(request,'pages/index.html',context)

def job_details(request):
    return render(request,'jobs/job_details.html')
def register(request):
    return render(request,'accounts/register.html')

def login(request):
    return render(request,'accounts/login.html')

def companies(request):
    company=Employeers.objects.all()
    context={
        'company':company
    }
    return render(request,'category/company.html',context)