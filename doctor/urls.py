from django.urls import path, include

from . import views

app_name = "doctor"
urlpatterns = [
    path('dashboard', views.Dash.as_view(), name='dashboard'),
    path('appointment', views.Appointment.as_view(), name='appointment'),
    path('appointment/past', views.PastAppointment.as_view(), name='past_appointments'),
    path('appointment/<int:pk>/update', views.UpdateAppointment.as_view(), name='update'),
    path('appointment/<int:pk>/cancel', views.CancelAppointment.as_view(), name='cancel'),
    path('appointment/<int:pk>/complete', views.CompleteAppointment.as_view(), name='complete'),
    path('appointment/<int:pk>/start', views.StartAppointment.as_view(), name='start'),
    path('patient/<int:id>', views.Patient_detail.as_view(), name='patient_detail'),
    path('chest-analysis', views.Analysis.as_view(), name='analysis')
    
]