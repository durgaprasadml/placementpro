from django.db import models

from drives.models import Drive
from students.models import Student


class Application(models.Model):
    class Status(models.TextChoices):
        APPLIED = 'applied', 'Applied'
        APTITUDE_CLEARED = 'aptitude_cleared', 'Aptitude Cleared'
        INTERVIEW_SCHEDULED = 'interview_scheduled', 'Interview Scheduled'
        SELECTED = 'selected', 'Selected'

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='applications')
    drive = models.ForeignKey(Drive, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.APPLIED)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'drive')

    def __str__(self):
        return f'{self.student} -> {self.drive} [{self.status}]'
