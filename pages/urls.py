from django.urls import path

from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('jobs/',views.jobs,name='jobs'),
    path('job_details/',views.job_details,name='job_details'),
    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
]