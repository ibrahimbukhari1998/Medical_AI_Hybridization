from dataclasses import Field
from django import forms
from django.forms import ModelForm
from django.core.validators import FileExtensionValidator

from core.models import Appointment, Radreport, Referal

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from crispy_bootstrap5.bootstrap5 import FloatingField



class RadReportForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(


            Row(
                Column(FloatingField('rad_type', css_class='form-group col-md-6 mb-0 hovercolor')),
                Column(FloatingField('body', css_class='form-group col-md-6 mb-0 hovercolor')),
                css_class='form-row'
            ),

            FloatingField('analysis', css_class="hovercolor"),
            FloatingField('comments', css_class="hovercolor"),
            FloatingField('rad_image', css_class="hovercolor"),
            
        )

    class Meta:
        model = Radreport
        fields = ["rad_types", "body", "analysis", "comments", "rad_image"]