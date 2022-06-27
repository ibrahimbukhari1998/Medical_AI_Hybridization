from django.contrib import admin
from .models import Appointment, Referal, Report, Radreport, Medreport


# FOR APPOINTMENT
class AppointmentAdmin(admin.ModelAdmin):
    ordering = ('-date',)
    list_display = ( 'patient', 'doctor', 'start_time', 'date', 'types', 'status' )

    fieldsets = (
        (None, {'fields': ('patient', 'doctor',)}),
        ('Date and Time', {'fields': ('date', 'start_time',)}),
        ('Details', {'fields': ('types', 'status', 'description',)}),
    )
    

admin.site.register(Appointment, AppointmentAdmin)





# FOR REFERALS 
class ReferalAdmin(admin.ModelAdmin):
    list_display = ( 'patient', 'doctor', 'radiologist', 'rad_types', 'body')

    fieldsets = (
        (None, {'fields': ('patient', 'doctor', 'radiologist',)}),
        ('Type and Location', {'fields': ('rad_types', 'body',)}),
        ('Details', {'fields': ('description', 'date', 'status', 'radrep',)}),
    )
    

admin.site.register(Referal, ReferalAdmin)





# FOR REPORTS
class ReportAdmin(admin.ModelAdmin):
    list_display = ( 'patient', 'date', 'report_type')

    fieldsets = (
        (None, {'fields': ('patient', 'doctor', 'radiologist',)}),
        ('Type', {'fields': ('report_type', 'date',)}),
        # ('Details', {'fields': ('description',)}),
    )
    

admin.site.register(Report, ReportAdmin)


class RadreportAdmin(admin.ModelAdmin):
    list_display = ( 'patient', 'date', 'report_type')

    fieldsets = (
        (None, {'fields': ('patient', 'doctor', 'radiologist',)}),
        ('Type', {'fields': ('report_type', 'date',)}),
        ('Details', {'fields': ('rad_types', 'body', 'analysis', 'comments', 'rad_image',)}),
    )
    

admin.site.register(Radreport, RadreportAdmin)


class MedreportAdmin(admin.ModelAdmin):
    list_display = ( 'patient', 'date', 'report_type')

    fieldsets = (
        (None, {'fields': ('patient', 'doctor', 'radiologist',)}),
        ('Type', {'fields': ('report_type', 'date',)}),
        ('Details', {'fields': ('visit_reason', 'analysis', 'comments', 'Prescription', 'med_image',)}),
    )
    

admin.site.register(Medreport, MedreportAdmin)