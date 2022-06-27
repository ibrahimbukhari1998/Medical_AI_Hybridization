from dateutil.relativedelta import relativedelta
from datetime import date
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _




class CustomManager(BaseUserManager):
    
    def create_user(self, email, username, first_name, password, **other_fields):
        
        if not email:
            raise ValueError(_('You must provide an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, first_name, password, **other_fields):
        
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, **other_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        
        if user.is_staff is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        
        return user
        
        
        
        
        
        

class CustomUser(AbstractBaseUser, PermissionsMixin):
    type_choices = (
        ('p', 'Patient'),
        ('d', 'Doctor'),
        ('r', 'Radiologist'),
        ('a', 'Admin')
    )
    
    
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)
    account_type = models.CharField('Type', max_length=100, choices=type_choices, default='a')
    date_joined = models.DateTimeField(default=timezone.now)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.jpg')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']
    
    objects = CustomManager()
    
    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)










class PatientManager(CustomManager):
    def get_queryset(self):
        return super().get_queryset().filter(account_type='p')


class DoctorManager(CustomManager):
    def get_queryset(self):
        return super().get_queryset().filter(account_type='d')


class RadiologistManager(CustomManager):
    def get_queryset(self):
        return super().get_queryset().filter(account_type='r')






Genders = (
    ('m', 'Male'),
    ('f', 'Female'),
)

class Patient(CustomUser):
    objects = PatientManager()
    
    gender = models.CharField('Gender', max_length=50, choices=Genders, default='m')
    dob = models.DateField('Date Of Birth', null=True)


    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name) 

    def save(self, *args, **kwargs):
        if not self.pk:
            self.account_type = 'p'
        return super().save(*args, **kwargs)

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    
    def get_age(self):
        now = date.today()
        rdelta = relativedelta(now, self.dob)
        return rdelta.years






SPECS = (
    ('gp', 'General Physician'),
    ('p', 'Pulmonology'),
    ('r', 'Radiology'),
    ('o', 'Oncology'),    
)

class Doctor(CustomUser):
    objects = DoctorManager()
    specialization = models.CharField('Specialization', max_length=500, choices=SPECS, default='gp')
    pmc = models.CharField('PMC Registeration No', max_length=100)


    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.account_type = 'd'
        return super().save(*args, **kwargs)

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)







class Radiologist(CustomUser):
    objects = RadiologistManager()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.account_type = 'r'
        return super().save(*args, **kwargs)

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
