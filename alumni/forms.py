from django import forms

from .models import ReferralPost


class ReferralPostForm(forms.ModelForm):
    class Meta:
        model = ReferralPost
        fields = ['title', 'description', 'apply_link']
