from django.shortcuts import redirect, render
from . forms import *
from django.views.generic import CreateView
from django.contrib.auth import login

# Create your views here.



class signupEmployers(CreateView):
    model = User
    form_class = SignUpFormEmployers
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

def signupUser(request):
    pass 