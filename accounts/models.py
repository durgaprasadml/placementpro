from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    class Role(models.TextChoices):
        STUDENT = 'student', 'Student'
        TPO = 'tpo', 'TPO'
        ALUMNI = 'alumni', 'Alumni'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=Role.choices)

    def __str__(self):
        return f'{self.user.username} ({self.role})'
