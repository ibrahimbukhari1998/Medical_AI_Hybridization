from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic.edit import UpdateView, DeleteView


from django.contrib import messages
from .forms import addAppoint
from register.models import Patient, Doctor, Radiologist
from core.models import Appointment as apt
from core.models import Radreport as rrep
from core.models import Medreport as mrep




# DASHBOARD INDEX VIEW
class Dash(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        # list = apt.objects.filter(doctor.email == request.user.email)
        
        if request.user.account_type == 'p':
            return render(request, 'patient/dashboard.html', {'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')





# ALL APPOINTMENT LIST VIEW
class Appointment(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'p':
            list = apt.objects.filter(patient=request.user).exclude(status='completed').exclude(status='cancelled').order_by('-date', '-start_time')
            return render(request, 'patient/appointment.html', {'list':list, 'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')




# PAST APPOINTMENTS
class PastAppointment(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'p':
            list = apt.objects.filter(patient=request.user).exclude(status='pending').exclude(status='confirmed').order_by('-date', '-start_time')
            return render(request, 'patient/past_appointments.html', {'list':list, 'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')




# ADD APPOINTMENT
class AddAppointment(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def check(self, doc, appoints):
        x=0
        for apt in appoints:
            
            if apt.doctor == doc and (apt.status == 'pending' or apt.status == 'confirmed') :
                x = x+1
        
        if x >= 3:
            return True
        else:
            return False
    
    
    def get(self, request):
        if request.user.account_type == 'p':
            doc_list = Doctor.objects.filter(is_active=True)
            appoints = apt.objects.filter(patient=request.user).exclude(status='completed').exclude(status='cancelled')
            form = addAppoint()
            ctx = {'form':form, 'list':doc_list, 'appoint':appoints, 'type':request.user.account_type}
            return render(request, 'patient/addAppointment.html', ctx)
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')
    
    
    def post(self, request):
        if request.user.account_type == 'p':
            pat = Patient.objects.get(pk=request.user.id)
            doc_list = Doctor.objects.filter(is_active=True)
            appoints = apt.objects.filter(patient=request.user).exclude(status='completed').exclude(status='cancelled')
            docid = request.POST.get("id")
            doc = Doctor.objects.get(pk=docid)
            form = addAppoint(request.POST)
            
            if not form.is_valid():
                ctx = {'form':form, 'list':doc_list, 'appoint':appoints, 'type':request.user.account_type}
                return render(request, 'patient/addAppointment.html', ctx)
            
            if self.check(doc, appoints):
                messages.success(request, 'Sorry! You can\'t schedule more than 3 appointments at a time ')
                return redirect('Patient:add_appointment')
            
            add = form.save(commit=False)
            add.patient = pat
            add.doctor = Doctor.objects.get(pk=docid)
            add.status = 'pending'
            add.save()
            
            messages.success(request, 'Appointment Request has been successfully sent ')
            return redirect('Patient:dashboard')
        




# CANCEL APPOINTMENT
class CancelAppointment(LoginRequiredMixin, View):
    login_url = '/login/'
    
    
    def get(self, request, pk):
        if request.user.account_type == 'p':
            appoint = get_object_or_404(apt, pk=pk)
            appoint.status = 'cancelled'
            appoint.save()
            return redirect('Patient:appointment')
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')






# REPORTS 
class Reports(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'p':
            pat = Patient.objects.get(pk=request.user.id)
            radReport = rrep.objects.filter(patient=pat).order_by('-date')
            medReport = mrep.objects.filter(patient=pat).order_by('-date')
            return render(request, 'patient/Reports.html', {'rrep':radReport, 'mrep':medReport, 'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')