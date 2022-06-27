from django.urls import path, include

from . import views

app_name = "Patient"
urlpatterns = [
    path('dashboard', views.Dash.as_view(), name='dashboard'),
    path('appointment', views.Appointment.as_view(), name='appointment'),
    path('appointment/past', views.PastAppointment.as_view(), name='past_appointments'),
    path('appointment/add', views.AddAppointment.as_view(), name='add_appointment'),
    path('appointment/<int:pk>/cancel', views.CancelAppointment.as_view(), name='cancel'),
    path('reports', views.Reports.as_view(), name='reports'),
]