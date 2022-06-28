from django.urls import path, include

from . import views

app_name = "administrator"
urlpatterns = [
    path('dashboard', views.Dash.as_view(), name='dashboard'),
    path('users', views.User.as_view(), name='users'),
    path('appointments', views.Appointment.as_view(), name='appointments'),
    path('reports', views.Report.as_view(), name='reports'),
    path('referals', views.Referal.as_view(), name='referals'),
    path('users/<int:id>/details', views.Account_detail.as_view(), name='account_detail'),
    path('users/<int:id>/delete', views.DeleteUser.as_view(), name='delete_user'),
    path('appointments/<int:id>/details', views.Appointment_detail.as_view(), name='appointment_detail'),
    path('appointments/<int:id>/delete', views.DeleteAppointment.as_view(), name='delete_appointment'),
    path('appointment/add', views.AddAppointment.as_view(), name='appointment_add'),
    path('reports/<int:id>/details', views.Report_detail.as_view(), name='reports_detail'),
    path('reports/<int:id>/delete', views.DeleteReport.as_view(), name='delete_reports'),
    path('reports/rad/add', views.AddRadReport.as_view(), name='radreport_add'),
    path('reports/med/add', views.AddMedReport.as_view(), name='medreport_add'),
    path('referals/<int:id>/detail', views.Referal_detail.as_view(), name='referal_detail'),
    path('referals/<int:id>.delete', views.DeleteReferal.as_view(), name='delete_referal'),
    path('referals/add', views.AddReferal.as_view(), name='referal_add'),
    
]