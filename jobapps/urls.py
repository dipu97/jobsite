from django.urls import path
from .import views

urlpatterns = [
    path('jobs/',views.jobs,name="jobs"),
    path('<int:JobPost_id>/', views.job_index, name='job_index'),
    path('job_post',views.job_post,name='job_post'),
    path('search/',views.search,name='search'),
    path('apply_for_job/', views.applyForJob,name='apply_for_job'),
    path ('about/', views.aboutUs,name='about'),
    path ('contact/', views.contactUs,name='contact'),
]
