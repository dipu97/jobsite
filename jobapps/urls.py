from django.urls import path
from .import views

urlpatterns = [
    path('jobs/',views.jobs,name="jobs"),
    path('<int:JobPost_id>/', views.job_index, name='job_index'),
    path('job_post',views.job_post,name='job_post'),

]
