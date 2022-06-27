from django import forms
from django.forms import ModelForm

from core.models import Appointment, Medreport, Referal

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from crispy_bootstrap5.bootstrap5 import FloatingField

class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class DatePickerInput(forms.DateInput):
        input_type = 'date'

class addAppoint(ModelForm):
    
    date = forms.DateField(widget=DatePickerInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(

            FloatingField('date', css_class="hovercolor"),
            FloatingField('types', css_class="hovercolor"),
            FloatingField('description', css_class="hovercolor"),
            
        )
    
    class Meta:
        model = Appointment
        fields=('date', 'types', 'description')