from datetime import date
from django.db import models
from register.models import Patient, Radiologist, Doctor



# APPOINTMENT MODEL
TYPES = (('consult', 'Consultation'), ('follow', 'Follow-up'),)
STATUS = (('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed'), ('cancelled', 'Cancelled'),)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, related_name='appoint_patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, related_name='appoint_doctor')
    description = models.TextField()
    date = models.DateField('Date')
    start_time = models.TimeField('Start Time', null=True)
    types = models.CharField(max_length=100, choices=TYPES)
    status = models.CharField(max_length=100, choices=STATUS)
    mcheck = models.BooleanField(default=False)
    rcheck = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)




# GLOBAL VARIABLES
Rad_types = (
    ('x', 'X-Ray'),
    ('ct', 'CT-Scan'),
    ('mri', 'MRI'),
    ('ot', 'Others'),
)

Body_location = (
    ('ab', 'Abdomen'),
    ('ch', 'Chest'),
    ('pl', 'Pelvis'),
    ('ue', 'Upper Extremities'),
    ('le', 'Lower Extremities'),
    ('sp', 'Spine'),
    ('hnf', 'Head, Neck and Face'),
    ('ot', 'Others'),
)




# REPORTS MODEL
Rep_type = (
    ('rad', 'Radiology'),
    ('med', 'Medical'),
)

class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, related_name='report_patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='report_doctor')
    radiologist = models.ForeignKey(Radiologist, on_delete=models.SET_NULL, null=True, blank=True, related_name='report_radiologist')
    report_type = models.CharField('Report Type', max_length=100, choices=Rep_type)
    date = models.DateField('Date', default=date.today)
    analysis = models.TextField('Analysis', null=True, blank=True)
    comments = models.TextField('Comments', null=True, blank=True)
    
    def __str__(self):
        return str(self.report_type)



class RadManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(report_type='rad')

class MedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(report_type='med')



class Radreport(Report):
    objects = RadManager()
    rad_types = models.CharField('Test Type', max_length=100, choices=Rad_types, default='ot')
    body = models.CharField('Body Location', max_length=100, choices=Body_location, default='ot')
    rad_image = models.ImageField(upload_to='rad_reports/', null = True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.report_type = 'rad'
        return super().save(*args, **kwargs)


class Medreport(Report):
    objects = MedManager()
    visit_reason = models.TextField('Visit Reason', null = True, blank=True)
    Prescription = models.TextField('Prescription', null = True, blank=True)
    med_image = models.ImageField(upload_to='med_reports/', null = True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.report_type = 'med'
        return super().save(*args, **kwargs)






# REFERAL MODAL
ref_status = (
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled')
)

class Referal(models.Model):
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True, related_name='referal_patient')
        rad_report = models.ForeignKey(Radreport, on_delete=models.SET_NULL, null=True, blank=True, related_name='rad_report')
        doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='referal_doctor')
        radiologist = models.ForeignKey(Radiologist, on_delete=models.SET_NULL, null=True, blank=True, related_name='referal_radiologist')
        rad_types = models.CharField('Test Type', max_length=100, choices=Rad_types, default='ot', blank=True)
        body = models.CharField('Body Location', max_length=100, choices=Body_location, default='ot', blank=True)
        description = models.TextField('Description', null=True, blank=True)
        status = models.CharField('Status', max_length=100, choices=ref_status, default='pending')
        date = models.DateField('Date', default=date.today)
        radrep = models.ForeignKey(Radreport, on_delete=models.DO_NOTHING, null=True, blank=True)
        
        def __str__(self):
            return str(self.rad_types)