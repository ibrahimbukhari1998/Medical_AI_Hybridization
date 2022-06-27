from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from pathlib import Path



from django.contrib import messages
from .forms import RadReportForm
from doctor.forms import ImageUploadForm
from register.models import Patient, Doctor, Radiologist
from core.models import Referal as refer
from doctor.models import Tempstorage as tmp
from core.MLmodels import Classify as classify




# DASHBOARD INDEX VIEW
class Dash(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'r':
            return render(request, 'radiologist/dashboard.html', {'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')




# REFERAL VIEW
class Referal(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'r':
            list = refer.objects.filter(radiologist=request.user).exclude(status='completed').exclude(status='cancelled').order_by('-date')
            return render(request, 'radiologist/referal.html', {'list':list, 'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')




# REFERAL START VIEW
class ReferalStart(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request, pk):
        
        if request.user.account_type == 'r':
            ref = get_object_or_404(refer, pk=pk)
            form = RadReportForm()
            ctx = {'form':form, 'rid':ref.id, 'type':request.user.account_type}
            return render(request, 'radiologist/start_referal.html', ctx)
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')
    
    
    def post(self, request, pk):
        
        if request.user.account_type == 'r':
            ref = get_object_or_404(refer, pk=pk)
            form = RadReportForm(request.POST, request.FILES)
            
            if not form.is_valid():
                ctx = {'form':form, 'rid':ref.id, 'type':request.user.account_type}
                return render(request, 'radiologist/start_referal.html', ctx)
            
            report = form.save(commit=False)
            report.patient = ref.patient
            report.doctor = ref.doctor
            report.radiologist = ref.radiologist
            report.save()
            ref.radrep = report
            ref.status = 'completed'
            ref.save()
            return redirect("radiologist:referal")
            
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')




# PAST REFERAL VIEW
class PastReferal(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'r':
            list = refer.objects.filter(radiologist=request.user).exclude(status='pending').order_by('-date')
            return render(request, 'radiologist/past_referals.html', {'list':list, 'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')




# CANCEL REFERAL
class ReferalCancel(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    
    def get(self, request, pk):
        if request.user.account_type == 'r':
            rfr = get_object_or_404(refer, pk=pk)
            rfr.status = 'cancelled'
            rfr.save()
            return redirect('radiologist:referal')
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')




# CHEST ANALYSIS
# CHEXT X-RAY ANALYSIS
class Analysis(LoginRequiredMixin, View):
    
    login_url = '/login/'
    
    def get(self, request):
        
        if request.user.account_type == 'r':
            form = ImageUploadForm()
            return render(request, "radiologist/analysis.html", {'form':form, 'check':False, 'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')

    def post(self, request):
        
        if request.user.account_type == 'r':
            
            form = ImageUploadForm(request.POST, request.FILES)
            
            if not form.is_valid():
                return render(request, "radiologist/analysis.html", {'form':form, 'check':False, 'type':request.user.account_type})
            
            form.save()
            
            img = tmp.objects.last()
            
            
            fpath = img.image.url
            img.delete()
            result = classify(fpath)

            return render(request, "radiologist/analysis.html", {'img':fpath, 'result':result, 'check':True, 'form':form, 'type':request.user.account_type})
        else:
            messages.success(request, 'Yikes! Seems like you were accessing something you shouldn\'t have ')
            return redirect('core:landing')