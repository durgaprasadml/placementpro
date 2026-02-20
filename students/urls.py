from django.urls import path

from . import views

app_name = 'students'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('resume/', views.resume_pdf, name='resume_pdf'),
]
