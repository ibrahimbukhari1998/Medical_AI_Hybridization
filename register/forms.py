from sqlite3 import Date
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import Patient, Doctor, Radiologist
from fypDjango import settings


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from crispy_bootstrap5.bootstrap5 import FloatingField



class DateInput(forms.DateInput):
    input_type = 'date'

class PatientForm(UserCreationForm):
    
    dob = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=DateInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = "8 characters long. Letter, Numbers and Special Characters"
        self.fields['password2'].help_text = "Enter the same Password as before"

        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            Row(
                Column(FloatingField('first_name', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('last_name', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),

            Row(
                Column(FloatingField('gender', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('dob', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),
            
            HTML(""" <span style="color: red;">{{ form.gender.errors }}</span> """),
            HTML(""" <span style="color: red;">{{ form.dob.errors }}</span> <br>"""),

            FloatingField('username', css_class="hovercolor"),
            HTML(""" <span style="color: red;">{{ form.username.errors }}</span> """),
            
            FloatingField('email', css_class="hovercolor"),
            HTML(""" <span style="color: red;">{{ form.email.errors }}</span> """),

            Row(
                Column(FloatingField('password1', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('password2', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),
            
            HTML(""" <span style="color: red;">{{ form.password1.errors }}</span> """),
            HTML(""" <span style="color: red;">{{ form.password2.errors }}</span> <br>"""),

            Submit('submit', 'Sign up as a Patient')
        )

    class Meta:
        model = Patient
        fields = ["first_name", "last_name", "gender", "dob", "username", "email", "password1", "password2"]






class DoctorForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = "8 characters long. Letter, Numbers and Special Characters"
        self.fields['password2'].help_text = "Enter the same Password as before"

        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            Row(
                Column(FloatingField('first_name', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('last_name', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),
            
            FloatingField('specialization', css_class="hovercolor"),
            
            FloatingField('pmc', css_class="hovercolor"),

            FloatingField('username', css_class="hovercolor"),
            HTML(""" <span style="color: red;">{{ form.username.errors }}</span> """),
            
            FloatingField('email', css_class="hovercolor"),
            HTML(""" <span style="color: red;">{{ form.email.errors }}</span> """),

            Row(
                Column(FloatingField('password1', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('password2', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),
            
            HTML(""" <span style="color: red;">{{ form.password1.errors }}</span> """),
            HTML(""" <span style="color: red;">{{ form.password2.errors }}</span> <br>"""),

            Submit('submit', 'Sign up as a Doctor')
        )

    class Meta:
        model = Doctor
        fields = ["first_name", "last_name", "username", "specialization", "pmc", "email", "password1", "password2"]





class RadiologistForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = "8 characters long. Letter, Numbers and Special Characters"
        self.fields['password2'].help_text = "Enter the same Password as before"

        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            Row(
                Column(FloatingField('first_name', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('last_name', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),
                        

            FloatingField('username', css_class="hovercolor"),
            HTML(""" <span style="color: red;">{{ form.username.errors }}</span> """),
            
            FloatingField('email', css_class="hovercolor"),
            HTML(""" <span style="color: red;">{{ form.email.errors }}</span> """),

            Row(
                Column(FloatingField('password1', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('password2', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),
            
            HTML(""" <span style="color: red;">{{ form.password1.errors }}</span> """),
            HTML(""" <span style="color: red;">{{ form.password2.errors }}</span> <br>"""),

            Submit('submit', 'Sign up as a Radiologist')
        )

    class Meta:
        model = Radiologist
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
