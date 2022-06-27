from django import forms
from django.forms import ModelForm

from .models import Appointment

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from crispy_bootstrap5.bootstrap5 import FloatingField





# class DateInput(forms.DateInput):
#     input_type = 'date'

# class AppointmentForm(ModelForm):
    
    
#     date = forms.DateField(widget=DateInput)
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)


#         self.helper = FormHelper()
#         self.helper.form_show_errors = False
#         self.helper.layout = Layout(
#             Row(
#                 Column(FloatingField('patient', css_class='form-group col-md-6 mb-0 hovercolor')),
#                 Column(FloatingField('doctor', css_class='form-group col-md-6 mb-0 hovercolor')),
#                 css_class='form-row'
#             ),
                        

#             FloatingField('date', css_class="hovercolor"),
#             HTML(""" <span style="color: red;">{{ form.date.errors }}</span> """),
            


#             Row(
#                 Column(FloatingField('types', css_class='form-group col-md-6 mb-0 hovercolor')),
#                 Column(FloatingField('status', css_class='form-group col-md-6 mb-0 hovercolor')),
#                 css_class='form-row'
#             ),
            
#             FloatingField('description', css_class="hovercolor"),

#             Submit('submit', 'Sign up as a Patient')
#         )



#     class Meta:
#         model = Appointment
#         fields = ["patient", "doctor", "description", "date", "types", "status"]