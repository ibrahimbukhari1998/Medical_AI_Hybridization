from django.urls import path, include

from . import views

app_name = "register"
urlpatterns = [
    path('', views.register, name='register'),
    path('doctor', views.Registerdoc.as_view(), name='doctor'),
    path('patient', views.Registerpat.as_view(), name='patient'),
    path('radiologist', views.Registerrad.as_view(), name='radiologist'),
    path('redirect', views.redirect_login.as_view(), name='redirect')
]