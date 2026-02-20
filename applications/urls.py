from django.urls import path

from . import views

app_name = 'applications'

urlpatterns = [
    path('apply/<int:drive_id>/', views.apply_drive, name='apply_drive'),
]
