from django.urls import path

from . import views

app_name = 'alumni'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('referrals/', views.referrals_feed, name='referrals_feed'),
]
