# from distutils.log import Log
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
# from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic.edit import UpdateView, DeleteView
import os
from pathlib import Path


from django.contrib import messages
# from .forms import TimeForm, MedReportForm, ReferalForm, ImageUploadForm
from register.models import Patient, Doctor, Radiologist
# from .models import Tempstorage as tmp
from core.models import Appointment as apt
from core.models import Radreport as rrep
from core.models import Medreport as mrep


#  GLOBAL VARIABLE
baseDr = Path(__file__).resolve().parent.parent



# DASHBOARD INDEX VIEW
class Dash(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        # list = apt.objects.filter(doctor.email == request.user.email)
        
        if request.user.account_type == 'a':
            return render(request, 'administrator/dashboard.html', {'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')


