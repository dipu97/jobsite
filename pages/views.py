from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def jobs(request):
    return render(request,'jobs/jobs.html')

def job_details(request):
    return render(request,'jobs/job_details.html')
def register(request):
    return render(request,'accounts/register.html')

def login(request):
    return render(request,'accounts/login.html')