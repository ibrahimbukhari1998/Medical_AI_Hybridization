from django.urls import path, include

from . import views

app_name = "radiologist"
urlpatterns = [
    path('dashboard', views.Dash.as_view(), name='dashboard'),
    path('chest-analysis', views.Analysis.as_view(), name='analysis'),
    path('referal', views.Referal.as_view(), name='referal'),
    path('referal/past', views.PastReferal.as_view(), name='past'),
    path('referal/<int:pk>/start', views.ReferalStart.as_view(), name='start'),
    path('referal/<int:pk>/cancel', views.ReferalCancel.as_view(), name='cancel'),
]