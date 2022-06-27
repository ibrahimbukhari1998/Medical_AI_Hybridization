from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PatientForm, DoctorForm, RadiologistForm

from django.contrib import messages



def register(request):
    return render(request, 'accounts/mdb_register.html')

class redirect_login(LoginRequiredMixin, View):
    
    def get(self, request):
        if request.user.account_type == 'd':
            return redirect('doctor:dashboard')
        elif request.user.account_type == 'p':
            return redirect('Patient:dashboard') 
        elif request.user.account_type == 'r':
            return redirect('radiologist:dashboard') 
        elif request.user.account_type == 'a':
            return redirect('administrator:dashboard')



# Create your views here.
class Registerdoc(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:landing')
        
        form = DoctorForm()
        ctx = {'form' : form, 'type':'d'}
        return render(request, 'accounts/register.html', ctx)
    
    
    def post(self, request):
        form = DoctorForm(request.POST)
        
        if not form.is_valid():
            ctx = {'form' : form, 'type':'d'}
            return render(request, 'accounts/register.html', ctx)
        
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Account was created for ' + user)
        return redirect('login')




class Registerpat(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:landing')
        
        form = PatientForm()
        ctx = {'form' : form, 'type':'p'}
        return render(request, 'accounts/register.html', ctx)
    
    
    def post(self, request):
        form = PatientForm(request.POST)
        
        if not form.is_valid():
            ctx = {'form' : form, 'type':'p'}
            return render(request, 'accounts/register.html', ctx)
        
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Account was created for ' + user)
        return redirect('login')




class Registerrad(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:landing')
        
        form = RadiologistForm()
        ctx = {'form' : form, 'type':'r'}
        return render(request, 'accounts/register.html', ctx)
    
    
    def post(self, request):
        form = RadiologistForm(request.POST)
        
        if not form.is_valid():
            ctx = {'form' : form, 'type':'r'}
            return render(request, 'accounts/register.html', ctx)
        
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Account was created for ' + user)
        return redirect('login')
    
    
