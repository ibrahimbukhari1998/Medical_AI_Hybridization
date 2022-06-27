from django.urls import path, include

from . import views

app_name = "administrator"
urlpatterns = [
    path('dashboard', views.Dash.as_view(), name='dashboard'),
]