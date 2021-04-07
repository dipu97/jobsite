from django.urls import path
from . import views

urlpatterns = [
    path('signup/employers/',views.signupEmployers.as_view(),name="singupemployers"),
    path('signup/user/',views.signupUser.as_view(),name="singupuser"),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),
]
