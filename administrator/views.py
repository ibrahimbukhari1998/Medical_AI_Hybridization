from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
import os
from pathlib import Path


from django.contrib import messages
from .forms import PatientForm, DoctorForm, RadiologistForm, AppointmentForm, MedReportForm, RadReportForm
from register.models import Patient, Doctor, Radiologist, CustomUser
from core.models import Appointment as apt
from core.models import Radreport as rrep
from core.models import Medreport as mrep
from core.models import Report as trep


#  GLOBAL VARIABLE
baseDr = Path(__file__).resolve().parent.parent



# DASHBOARD INDEX VIEW
class Dash(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'a':
            return render(request, 'administrator/dashboard.html', {'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')










# USERS LIST VIEW
class User(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'a':
            
            usr = CustomUser.objects.all().exclude(account_type='a')
            return render(request, 'administrator/users.html', {'list':usr, 'type':request.user.account_type}) 
            
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')




# USER ACCOUNT DETAIL
class Account_detail(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    
    def get(self, request, id):
        
        if request.user.account_type == 'a':
        
            cuser = CustomUser.objects.get(pk=id)
            if cuser.account_type == 'p':
                
                pat = Patient.objects.get(pk=id)
                pform = PatientForm(instance = pat)
                
                return render(request, "administrator/user_detail.html", {'form':pform, 'type':request.user.account_type, 'user_type':cuser.account_type, 'user_id':cuser.id})
                
            elif cuser.account_type == 'd':
                
                doc = Doctor.objects.get(pk=id)
                dform = DoctorForm(instance = doc)
                
                return render(request, "administrator/user_detail.html", {'form':dform, 'type':request.user.account_type, 'user_type':cuser.account_type, 'user_id':cuser.id})
                
            elif cuser.account_type == 'r':
                
                rad = Radiologist.objects.get(pk=id)
                rform = RadiologistForm(instance = rad)
                
                return render(request, "administrator/user_detail.html", {'form':rform, 'type':request.user.account_type, 'user_type':cuser.account_type, 'user_id':cuser.id})
        
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')
    
    
    def post(self, request, id):
        
        if request.user.account_type == 'a':
        
            cuser = CustomUser.objects.get(pk=id)
            if cuser.account_type == 'p':
                
                pat = Patient.objects.get(pk=id)
                form = PatientForm(request.POST, instance=pat)
                
                if not form.is_valid():
                    return render(request, "administrator/user_detail.html", {'form':form, 'type':request.user.account_type, 'user_type':cuser.account_type, 'user_id':cuser.id})
                else:
                    form.save()
                    return redirect("administrator:users")
                
            elif cuser.account_type == 'd':
                
                doc = Doctor.objects.get(pk=id)
                dform = DoctorForm(request.POST, instance=doc)
                if not dform.is_valid():
                    return render(request, "administrator/user_detail.html", {'form':dform, 'type':request.user.account_type, 'user_type':cuser.account_type, 'user_id':cuser.id})
                
                dform.save()
                return redirect("administrator:users")
                
            elif cuser.account_type == 'r':
                
                rad = Radiologist.objects.get(pk=id)
                rform = RadiologistForm(request.POST, instance=rad)
                if not rform.is_valid():
                    return render(request, "administrator/user_detail.html", {'form':rform, 'type':request.user.account_type, 'user_type':cuser.account_type, 'user_id':cuser.id})
                
                rform.save()
                return redirect("administrator:users")
        
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')




# DELETE USER ACCOUNT
class DeleteUser(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request, id):
        
        if request.user.account_type == 'a':
            cuser = CustomUser.objects.get(pk=id)
            cuser.delete()
            return redirect("administrator:users")
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')











# APPOINTMENTS LIST VIEW
class Appointment(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'a':
            
            appoint = apt.objects.all().order_by('-date', '-start_time')
            return render(request, 'administrator/appointments.html', {'list':appoint, 'type':request.user.account_type}) 
            
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')
        




# APPOINTMENT DETAIL
class Appointment_detail(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request, id):
        
        if request.user.account_type == 'a':
            
            appoint = apt.objects.get(pk=id)
            form = AppointmentForm(instance=appoint)
            return render(request, 'administrator/appointments_detail.html', {'form':form, 'type':request.user.account_type, 'appoint_id':appoint.id}) 
            
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')
        
        
    def post(self, request, id):
        
        if request.user.account_type == 'a':
            
            appoint = apt.objects.get(pk=id)
            form = AppointmentForm(request.POST, instance=appoint)
            
            if not form.is_valid():
                return render(request, 'administrator/appointments_detail.html', {'form':form, 'type':request.user.account_type, 'appoint_id':appoint.id})  
            
            form.save()
            return redirect("administrator:appointments")
        
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')




# DELETE APPOINTMENT
class DeleteAppointment(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request, id):
        
        if request.user.account_type == 'a':
                appoint = apt.objects.get(pk=id)
                appoint.delete()
                return redirect("administrator:appointments")
        
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')




# ADD APPOINTMENT
class AddAppointment(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'a':
            form = AppointmentForm()
            return render(request, "administrator/Add_appointment.html", {'form':form, 'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')

    def post(self, request):
        
        form = AppointmentForm(request.POST)
        
        if not form.is_valid():
            return render(request, "administrator/Add_appointment.html", {'form':form, 'type':request.user.account_type})
        
        form.save()
        messages.success(request, 'Appointment has been successfully created')
        return redirect("administrator:appointments")









# REPORTS LIST VIEW
class Report(LoginRequiredMixin, View):
    
    def get(self, request):
        
        if request.user.account_type == 'a':
            
            rep = trep.objects.all().order_by('-date')
            return render(request, 'administrator/reports.html', {'list':rep, 'type':request.user.account_type}) 
            
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')



# REPORT DETAIL
class Report_detail(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    
    def get(self, request, id):
        
        if request.user.account_type == 'a':
        
            rep = trep.objects.get(pk=id)
            if rep.report_type == 'rad':
                
                radrep = rrep.objects.get(pk=id)
                rform = RadReportForm(instance = radrep)
                
                return render(request, "administrator/reports_detail.html", {'form':rform, 'type':request.user.account_type, 'report_type':rep.report_type, 'report_id':rep.id})
                
            elif rep.report_type == 'med':
                
                medrep = mrep.objects.get(pk=id)
                mform = MedReportForm(instance = medrep)
                
                return render(request, "administrator/reports_detail.html", {'form':mform, 'type':request.user.account_type, 'report_type':rep.report_type, 'report_id':rep.id})
            
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')
    
    
    def post(self, request, id):
        
        if request.user.account_type == 'a':
        
            rep = trep.objects.get(pk=id)
            if rep.report_type == 'rad':
                
                radrep = rrep.objects.get(pk=id)
                rform = RadReportForm(request.POST, request.FILES, instance = radrep)
                
                if not rform.is_valid():
                    return render(request, "administrator/reports_detail.html", {'form':rform, 'type':request.user.account_type, 'report_type':rep.report_type, 'report_id':rep.id})
                
                rform.save()
                return redirect("administrator:reports")
                
            elif rep.report_type == 'med':
                
                medrep = mrep.objects.get(pk=id)
                mform = MedReportForm(instance = medrep)
                
                if not mform.is_valid():
                    return render(request, "administrator/reports_detail.html", {'form':mform, 'type':request.user.account_type, 'report_type':rep.report_type, 'report_id':rep.id})
                
                mform.save()
                return redirect("administrator:reports")
            
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')




# REPORT ADD
class AddRadReport(LoginRequiredMixin, View):
    
    
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'a':
            form = RadReportForm()
            return render(request, "administrator/Add_radreport.html", {'form':form, 'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')


    def post(self, request):
        
        form = RadReportForm(request.POST, request.FILES)
        
        if not form.is_valid():
            return render(request, "administrator/Add_radreport.html", {'form':form, 'type':request.user.account_type})
        
        form.save()
        messages.success(request, 'Report has been successfully created')
        return redirect("administrator:reports")




# REPORT ADD
class AddMedReport(LoginRequiredMixin, View):
    
    
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'a':
            form = MedReportForm()
            return render(request, "administrator/Add_medreport.html", {'form':form, 'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')


    def post(self, request):
        
        form = MedReportForm(request.POST, request.FILES)
        
        if not form.is_valid():
            return render(request, "administrator/Add_medreport.html", {'form':form, 'type':request.user.account_type})
        
        form.save()
        messages.success(request, 'Appointment has been successfully created')
        return redirect("administrator:reports")




# DELETE REPORT
class DeleteReport(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request, id):
        
        if request.user.account_type == 'a':
                rep = trep.objects.get(pk=id)
                rep.delete()
                return redirect("administrator:reports")
        
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')












# REFERAL LIST VIEW
class Referal(LoginRequiredMixin, View):
    pass
