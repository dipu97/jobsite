from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import *
# Create your views here.
def jobs_list(request):
    number = JobPost.objects.all().count()
    dict_method=request.GET.copy()
    jobss = JobPost.objects.filter(is_published=True)
    paginator=Paginator(jobss,4)
    page=request.GET.get('page',1)
    try:
        paged_jobs=paginator.get_page(page)
    except PageNotAnInteger:
        paged_jobs=paginator.page(1)
    except EmptyPage:
        paged_jobs=paginator.page(paginator.num_pages)
    context = {
        'jobss': paged_jobs,
        'count':number,
        'get_method':dict_method,

    }
    return render(request, 'jobs/jobs.html', context)