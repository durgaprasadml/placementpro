from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('students/', include('students.urls')),
    path('drives/', include('drives.urls')),
    path('applications/', include('applications.urls')),
    path('alumni/', include('alumni.urls')),
]
