from dataclasses import Field
from django import forms
from django.forms import ModelForm
from django.core.validators import FileExtensionValidator

from core.models import Appointment, Medreport, Referal
from .models import Tempstorage

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from crispy_bootstrap5.bootstrap5 import FloatingField

class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class DatePickerInput(forms.DateInput):
        input_type = 'date'

class TimeForm(ModelForm):
    
    start_time = forms.TimeField(widget=TimePickerInput)
    date = forms.DateField(widget=DatePickerInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(

            FloatingField('date', css_class="hovercolor"),
            FloatingField('start_time', css_class="hovercolor"),
            
        )
    
    class Meta:
        model = Appointment
        fields=('date', 'start_time',)



class MedReportForm(forms.ModelForm):
    

    class Meta:
        model = Medreport
        fields = ["visit_reason", "analysis", "comments", "Prescription", "med_image"]



class ReferalForm(ModelForm):
    
    class Meta:
        model = Referal
        fields = ["radiologist", "rad_types", "body", "description"]


class ImageUploadForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(

            FloatingField('image', css_class="hovercolor"),
            FloatingField('start_time', css_class="hovercolor"),
            
        )
    
    class Meta:
        model = Tempstorage
        fields = ["image"]