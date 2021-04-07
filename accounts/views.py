from django.shortcuts import redirect, render
from . forms import *
from django.views.generic import CreateView
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.



class signupEmployers(CreateView):
    model = User
    form_class = SignUpFormEmployers
    template_name = 'accounts/employers/register.html'

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('/')

class signupUser(CreateView):
    model = User
    form_class = SignUpFormUsers
    template_name = 'accounts/jobseekers/register.html'

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('/')

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'accounts/employers/login.html',context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')