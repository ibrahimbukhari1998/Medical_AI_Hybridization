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
from .forms import TimeForm, MedReportForm, ReferalForm, ImageUploadForm
from register.models import Patient, Doctor, Radiologist
from .models import Tempstorage as tmp
from core.models import Appointment as apt
from core.models import Radreport as rrep
from core.models import Medreport as mrep

from core.MLmodels import Classify as classify
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


#  GLOBAL VARIABLE
baseDr = Path(__file__).resolve().parent.parent



# DASHBOARD INDEX VIEW
class Dash(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        # list = apt.objects.filter(doctor.email == request.user.email)
        
        if request.user.account_type == 'd':
            return render(request, 'doctor/dashboard.html', {'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')





# ALL APPOINTMENT LIST VIEW
class Appointment(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'd':
            list = apt.objects.filter(doctor=request.user).exclude(status='completed').exclude(status='cancelled').order_by('-date', '-start_time')
            return render(request, 'doctor/appointment.html', {'list':list, 'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')



class PastAppointment(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'd':
            list = apt.objects.filter(doctor=request.user).exclude(status='pending').exclude(status='confirmed').order_by('-date', '-start_time')
            return render(request, 'doctor/past_appointments.html', {'list':list, 'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')



# CONFIRM AND UPDATE APPOINTMENT
class UpdateAppointment(LoginRequiredMixin, View):
    
    login_url = '/login/'
    template = 'doctor/confirm_appointment.html'

    def get(self, request, pk):
        if request.user.account_type == 'd':     
            appoint = get_object_or_404(apt, pk=pk)
            form = TimeForm(instance=appoint)
            ctx = {'form': form, 'appoint':appoint, 'type':request.user.account_type}
            return render(request, self.template, ctx)
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')


    def post(self, request, pk):
        appoint = get_object_or_404(apt, pk=pk)
        form = TimeForm(request.POST, instance=appoint)
        if not form.is_valid():
            ctx = {'form': form, 'appoint':appoint, 'type':request.user.account_type}
            return render(request, 'doctor/confirm_appointment.html', ctx)
        
        appoint.status = 'confirmed'
        appoint.save()
        form.save()
        return redirect('doctor:appointment')



# CANCEL APPOINTMENT
class CancelAppointment(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request, pk):
        if request.user.account_type == 'd':
            appoint = get_object_or_404(apt, pk=pk)
            appoint.status = 'cancelled'
            appoint.save()
            return redirect('doctor:appointment')
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')




# START APPOINTMENT
class StartAppointment(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request, pk):
        if request.user.account_type == 'd':
            appoint = get_object_or_404(apt, pk=pk)
            pat = appoint.patient
            radReport = rrep.objects.filter(patient=pat).order_by('-date')
            medReport = mrep.objects.filter(patient=pat).order_by('-date')
            
            form = MedReportForm()
            form2 = ReferalForm()
            ctx = {'form':form, 'form2':form2, 'rrep':radReport, 'mrep':medReport, 'mcheck':appoint.mcheck, 'rcheck':appoint.rcheck, 'appoint':appoint, 'type':request.user.account_type}
            return render(request, 'doctor/start_appointment.html', ctx)
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')
    
    
    def post(self, request, pk):
        appoint = get_object_or_404(apt, pk=pk)
        form = MedReportForm(request.POST, request.FILES)
        form2 = ReferalForm(request.POST)
        
        appoint = get_object_or_404(apt, pk=pk)
        pat = appoint.patient
        radReport = rrep.objects.filter(patient=pat).order_by('-date')
        medReport = mrep.objects.filter(patient=pat).order_by('-date')
        
        if not form.is_valid() or not form2.is_valid():
            ctx = {'form': form, "form2":form2, 'rrep':radReport, 'mrep':medReport, 'mcheck':appoint.mcheck, 'rcheck':appoint.rcheck, 'appoint':appoint, 'type':request.user.account_type}
            return render(request, 'doctor/start_appointment.html', ctx)

        if request.POST.get("form_type") == 'medreport':
            report = form.save(commit=False)
            report.patient = appoint.patient
            report.doctor = appoint.doctor
            report.save()
            appoint.mcheck = True
            appoint.save()
            return redirect("doctor:start", pk=appoint.id)
        
        if request.POST.get("form_type") == 'referal':
            referal = form2.save(commit=False)
            referal.patient = appoint.patient
            referal.doctor = appoint.doctor
            referal.save()
            appoint.rcheck = True
            appoint.save()
            return redirect("doctor:start", pk=appoint.id)
            

        
        return redirect('doctor:appointment')



# COMPLETE APPOINTMENT
class CompleteAppointment(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request, pk):
        if request.user.account_type == 'd':
            appoint = get_object_or_404(apt, pk=pk)
            appoint.status = 'completed'
            appoint.save()
            return redirect('doctor:appointment')




# PATIENT REPORT HISTORY
class Patient_detail(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request, id):
        
        if request.user.account_type == 'd':
            pat = Patient.objects.get(pk=id)
            radReport = rrep.objects.filter(patient=pat).order_by('-date')
            medReport = mrep.objects.filter(patient=pat).order_by('-date')
            return render(request, 'doctor/patient_history.html', {'rrep':radReport, 'mrep':medReport, 'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')




# CHEXT X-RAY ANALYSIS
class Analysis(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'd':
            form = ImageUploadForm()
            return render(request, "doctor/analysis.html", {'form':form, 'check':False, 'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')

    def post(self, request):
        
        if request.user.account_type == 'd':
            
            form = ImageUploadForm(request.POST, request.FILES)
            
            if not form.is_valid():
                return render(request, "doctor/analysis.html", {'form':form, 'check':False, 'type':request.user.account_type})
            
            form.save()
            
            img = tmp.objects.last()
            
            
            fpath = img.image.url
            img.delete()
            result = classify(fpath)

            return render(request, "doctor/analysis.html", {'img':fpath, 'result':result, 'check':True, 'form':form, 'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')