from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction

from .models import *


class SignUpFormEmployers(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    company_name = forms.CharField(required=True)
    address = forms.CharField(required=True)
    company_description = forms.CharField(required=False)
    company_type = forms.CharField(required=False)
    website_url = forms.CharField(required=False)
    contact = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employeers = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        
        employers = Employeers.objects.create(user=user)
        employers.company_name=self.cleaned_data.get('company_name')
        employers.address=self.cleaned_data.get('address')
        employers.company_description=self.cleaned_data.get('company_description')
        employers.company_type=self.cleaned_data.get('company_type')
        employers.website_url = self.cleaned_data.get('website_url')
        employers.contact=self.cleaned_data.get('contact')
        
        employers.save()
        return user