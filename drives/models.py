from django.db import models


class Drive(models.Model):
    company_name = models.CharField(max_length=255)
    min_cgpa = models.FloatField()
    allowed_branches = models.TextField(help_text='Comma separated list of branches')
    max_backlogs = models.IntegerField(default=0)
    drive_date = models.DateField()

    def __str__(self):
        return f'{self.company_name} ({self.drive_date})'

    def parsed_branches(self):
        return [branch.strip().lower() for branch in self.allowed_branches.split(',') if branch.strip()]

    def is_student_eligible(self, student):
        """Criteria engine for drive eligibility."""
        return (
            student.cgpa >= self.min_cgpa
            and student.branch.strip().lower() in self.parsed_branches()
            and student.backlogs <= self.max_backlogs
        )
