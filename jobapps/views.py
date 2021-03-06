from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from jobapps.models import *
from accounts.models import *
from .model_choices import Category
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def jobs(request):
    number = JobPost.objects.all().count()
    dict_method = request.GET.copy()
    jobs = JobPost.objects.filter(is_published=True)
    paginator = Paginator(jobs, 4)
    page = request.GET.get('page', 1)
    try:
        paged_jobs = paginator.get_page(page)
    except PageNotAnInteger:
        paged_jobs = paginator.page(1)
    except EmptyPage:
        paged_jobs = paginator.page(paginator.num_pages)
    context = {
        'jobs': paged_jobs,
        'count': number,
        'get_method': dict_method,

    }
    return render(request, 'jobs/jobs.html', context)


def job_index(request, JobPost_id):
    job_index_ = JobPost.objects.get(id=JobPost_id)
    
    return render(request, 'jobs/job_details.html', {'job_index': job_index_})


# def job_post(request):
#
#     return render(request,'jobs/job_post.html')
@login_required
def job_post(request):
    if request.method == 'POST':
        dict_method = request.POST.copy()
        name = dict_method.get('name')
        title = dict_method.get('title')
        desc = dict_method.get('desc')
        requirements = dict_method.get('requirements')
        res = dict_method.get('res')
        experience = dict_method.get('experience')
        salary = dict_method.get('salary')
        benefit = dict_method.get('benefit')
        nature = dict_method.get('nature')
        location = dict_method.get('location')
        deadline = dict_method.get('deadline')
        process = dict_method.get('process')
        skills = dict_method.get('skills')
        JobPost.objects.create(user=name,
                               title=title,
                               job_description=desc,
                               job_requirements=requirements,
                               responsibilities=res,
                               exprience=experience,
                               salary=salary,
                               benefits=benefit,
                               job_nature=nature,
                               location=location,
                               deadline=deadline,
                               application_process=process,
                               skills=skills,
                               )
        messages.success(request, 'Job Posted Successfully')
        return HttpResponseRedirect(reverse('job_post'))
    return render(request, 'jobs/job_post.html')


def search(request):
    dict_method = request.GET.copy()

    Category = dict_method.get('Category') or None

    jobs = JobPost.objects.filter(is_published=True)
    paginator = Paginator(jobs, 4)
    page = request.GET.get('page', 1)
    try:
        paged_jobs = paginator.get_page(page)
    except PageNotAnInteger:
        paged_jobs = paginator.page(1)
    except EmptyPage:
        paged_jobs = paginator.page(paginator.num_pages)
    if 'Keyword' is not None:
        Keyword = dict_method.get('Keyword')
        jobs = JobPost.objects.filter(title__icontains=Keyword)

    if 'Location' in dict_method:
        Location = dict_method.get('Location')
        jobs = JobPost.objects.filter(location__icontains=Location)

    if 'Category' in dict_method:
        Category = dict_method.get('Category')
        jobs = JobPost.objects.filter(type__icontains=Category)

    context = {
        'jobs': jobs,
        'Category': Category,
        'get_method': dict_method,
        'jobss': paged_jobs,

    }

    return render(request, 'jobs/search.html', context)


@login_required
def applyForJob(request):
    # job_qs=JobPost.objects.get(id=id)
    # context={
    #     'job_qs':job_qs
    # }
    if request.method == 'POST':
        dict_method = request.POST.copy()
        name = dict_method.get('name')
        email = dict_method.get('mail')
        address = dict_method.get('address')
        image = dict_method.get('image')
        resume = dict_method.get('resume')
        cover_letter = dict_method.get('cover')
        salary = dict_method.get('salary')
        user = User.objects.get(user=email)
        job_id = dict_method.get('job_id') or None
        job_id = JobPost.objects.get(title=job_id)

        ApplyForJob.objects.create(
                                   name=name,
                                   email=email,
                                   address=address,
                                   image=image,
                                   resume=resume,
                                   cover_letter=cover_letter,
                                   salary_exceptation=salary,
                                   )
        messages.success(request, 'Job Applied Successfully')
        return HttpResponseRedirect(reverse('apply_for_job'))
    return render(request, 'jobs/apply_for_job.html')

def aboutUs(request):
    return render(request,'jobs/about.html')


def contactUs(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']

        message = request.POST['message']

        if Contact.objects.filter(email=email).exists():
            messages.error(request,'you already contact us')
        else:
            obj= Contact(name=name,email=email,message=message)
            obj.save()
            messages.success(request,'Successfully Send')
        return HttpResponseRedirect(reverse('contact'))
    return render(request,'jobs/contact.html')