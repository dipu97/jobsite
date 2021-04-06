from django.urls import path
from . import views

urlpatterns = [
    path('signup/employers/',views.signupEmployers.as_view(),name="singupemployers"),
    path('signup/user/',views.signupUser,name="singupuser"),
]
