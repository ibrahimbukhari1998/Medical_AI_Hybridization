from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Doctor, Patient, Radiologist


# FOR ALL USERS
class CustomUserAdmin(UserAdmin):
    ordering = ('-date_joined',)
    list_display = ( 'email', 'username', 'date_joined', 'is_active', 'account_type' )

    fieldsets = (
        (None, {'fields': ('email', 'username',)}),
        ('Name', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Account Info', {'fields': ('account_type', 'date_joined', 'profile_image',)}),
    )

add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)



# FOR DOCTOR USERS ONLY
class DoctorAdmin(UserAdmin):
    ordering = ('-date_joined',)
    list_display = ( 'email', 'username', 'specialization', 'date_joined', 'is_active', 'account_type' )

    fieldsets = (
        (None, {'fields': ('email', 'username', 'specialization', 'pmc',)}),
        ('Name', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Account Info', {'fields': ('account_type', 'date_joined', 'profile_image', )}),
    )

add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'specialization', 'pmc', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

admin.site.register(Doctor, DoctorAdmin)



# FOR PATIENT USERS ONLY
class PatientAdmin(UserAdmin):
    ordering = ('-date_joined',)
    list_display = ( 'email', 'username', 'date_joined', 'is_active', 'account_type' )

    fieldsets = (
        (None, {'fields': ('email', 'username',)}),
        ('Info', {'fields': ('first_name', 'last_name', 'gender', 'dob',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Account Info', {'fields': ('account_type', 'date_joined', 'profile_image',)}),
    )


add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'gender', 'dob', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )


admin.site.register(Patient, PatientAdmin)




# FOR RADIOLOGIST USERS ONLY 
class RadiologistAdmin(UserAdmin):
    ordering = ('-date_joined',)
    list_display = ( 'email', 'username', 'date_joined', 'is_active', 'account_type' )

    fieldsets = (
        (None, {'fields': ('email', 'username',)}),
        ('Name', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Account Info', {'fields': ('account_type', 'date_joined', 'profile_image',)}),
    )


add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

admin.site.register(Radiologist, RadiologistAdmin)
