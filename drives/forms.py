from django import forms

from .models import Drive


class DriveForm(forms.ModelForm):
    class Meta:
        model = Drive
        fields = ['company_name', 'min_cgpa', 'allowed_branches', 'max_backlogs', 'drive_date']
        widgets = {
            'drive_date': forms.DateInput(attrs={'type': 'date'}),
        }
