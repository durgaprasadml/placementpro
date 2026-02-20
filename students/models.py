from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    # Requirement asks for a ForeignKey user relation.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_profiles')
    cgpa = models.FloatField(default=0)
    branch = models.CharField(max_length=100)
    backlogs = models.IntegerField(default=0)
    skills = models.TextField(help_text='Comma separated skills')
    projects = models.TextField()

    def __str__(self):
        return f'{self.user.get_full_name() or self.user.username} - {self.branch}'
