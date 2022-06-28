# from sqlite3 import Date
from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

from register.models import Patient, Doctor, Radiologist
from core.models import Appointment, Medreport, Radreport
from fypDjango import settings


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from crispy_bootstrap5.bootstrap5 import FloatingField



class DateInput(forms.DateInput):
    input_type = 'date'

class TimePickerInput(forms.TimeInput):
        input_type = 'time'

# PATIENT FORM
class PatientForm(forms.ModelForm):
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            
            Row(
                Column(FloatingField('first_name', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('last_name', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),

            HTML(""" <br> """),

            Row(
                Column(FloatingField('gender', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('dob', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),
            
            HTML(""" <br> """),
            HTML(""" <span style="color: red;">{{ form.gender.errors }}</span> """),


            FloatingField('username', css_class="hovercolor"),
            HTML(""" <span style="color: red;">{{ form.username.errors }}</span> """),
            
            FloatingField('email', css_class="hovercolor"),
            HTML(""" <span style="color: red;">{{ form.email.errors }}</span> """),
            
            HTML(""" <br> """),
            FloatingField('account_type', css_class="hovercolor"),
            
            'is_active',

            HTML(""" <div class='text-center'> """),
            Submit('submit', 'Save and Update'),
            HTML(""" </div> """),

        )

    class Meta:
        model = Patient
        fields = ["first_name", "last_name", "gender", "dob", "username", "email", "account_type", "is_active"]
        widgets = {
            'dob': DateInput(),
        }



# DOCTOR FORM
class DoctorForm(forms.ModelForm):
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            
            Row(
                Column(FloatingField('first_name', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('last_name', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),

            HTML(""" <br> """),

            Row(
                Column(FloatingField('specialization', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('pmc', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),
            
            HTML(""" <br> """),

            FloatingField('username', css_class="hovercolor"),
            HTML(""" <span style="color: red;">{{ form.username.errors }}</span> """),
            
            FloatingField('email', css_class="hovercolor"),
            HTML(""" <span style="color: red;">{{ form.email.errors }}</span> """),
            
            HTML(""" <br> """),
            FloatingField('account_type', css_class="hovercolor"),
            
            'is_active',
            
            HTML(""" <div class='text-center'> """),
            Submit('submit', 'Save and Update'),
            HTML(""" </div> """),


        )

    class Meta:
        model = Doctor
        fields = ["first_name", "last_name", "specialization", "pmc", "username", "email", "account_type", "is_active"]
        widgets = {
            'dob': DateInput(),
        }



# RADIOLOGIST FORM
class RadiologistForm(forms.ModelForm):
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            
            Row(
                Column(FloatingField('first_name', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('last_name', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),

            HTML(""" <br> """),

            FloatingField('username', css_class="hovercolor"),
            HTML(""" <span style="color: red;">{{ form.username.errors }}</span> """),
            
            FloatingField('email', css_class="hovercolor"),
            HTML(""" <span style="color: red;">{{ form.email.errors }}</span> """),
            
            HTML(""" <br> """),
            FloatingField('account_type', css_class="hovercolor"),
            
            'is_active',
            
            HTML(""" <div class='text-center'> """),
            Submit('submit', 'Save and Update'),
            HTML(""" </div> """),
        )

    class Meta:
        model = Radiologist
        fields = ["first_name", "last_name", "username", "email", "account_type", "is_active"]
        widgets = {
            'dob': DateInput(),
        }







# Appointment Form
class AppointmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            
            FloatingField('patient', css_class="hovercolor"),
            FloatingField('doctor', css_class="hovercolor"),   
            
            HTML(""" <br> """),
            Row(
                Column(FloatingField('date', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('start_time', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),
            HTML(""" <br> """),
            
            
            Row(
                Column(FloatingField('types', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('status', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),
            HTML(""" <br> """),

            FloatingField('description', css_class="hovercolor"),            
            
            HTML(""" <div class='text-center'> """),
            Submit('submit', 'Save'),
            HTML(""" </div> """),
        )

    class Meta:
        model = Appointment
        fields = ["patient", "doctor", "date", "start_time", "types", "status", "description"]
        widgets = {
            'date': DateInput(),
            'start_time': TimePickerInput()
        }








# REPORT FORM
class MedReportForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            
            FloatingField('patient', css_class="hovercolor"),
            FloatingField('doctor', css_class="hovercolor"),   
            
            HTML(""" <br> """),
            Row(
                Column(FloatingField('report_type', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('date', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),
            HTML(""" <br> """),
            
            'visit_reason',
            'analysis',
            'comments',
            'Prescription',            

            HTML(""" <br> """),

    
            'med_image',
                        
            HTML(""" <div class='text-center'> """),
            Submit('submit', 'Save'),
            HTML(""" </div> """),
        )

    class Meta:
        model = Medreport
        fields = ["patient", "doctor", "report_type", "date", "visit_reason", "analysis", "comments", "Prescription", "med_image"]
        widgets = {
            'date': DateInput(),
            # 'start_time': TimePickerInput()
        }


# REPORT FORM
class RadReportForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            
            Row(
                Column(FloatingField('patient', css_class='form-group col-md-4 mb-0 hovercolor')),
                Column(FloatingField('doctor', css_class='form-group col-md-4 mb-0 hovercolor')),
                Column(FloatingField('radiologist', css_class='form-group col-md-4 mb-0 hovercolor')),
                css_class='form-row'
            ), 
            
            HTML(""" <br> """),
            Row(
                Column(FloatingField('report_type', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('date', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),
            HTML(""" <br> """),
            
            
            Row(
                Column(FloatingField('rad_types', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('body', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),
            HTML(""" <br> """),
            
            'analysis',
            'comments',

            HTML(""" <br> """),

            'rad_image',            
            
            HTML(""" <div class='text-center'> """),
            Submit('submit', 'Save'),
            HTML(""" </div> """),
        )

    class Meta:
        model = Radreport
        fields = ["patient", "doctor", "radiologist", "report_type", "date", "rad_types", "body", "analysis", "comments", "rad_image"]
        widgets = {
            'date': DateInput(),
        }