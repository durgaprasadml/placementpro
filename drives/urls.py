from django.urls import path

from . import views

app_name = 'drives'

urlpatterns = [
    path('tpo/dashboard/', views.tpo_dashboard, name='tpo_dashboard'),
]
