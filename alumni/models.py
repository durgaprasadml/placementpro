from django.contrib.auth.models import User
from django.db import models


class AlumniProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alumni_profiles')
    organization = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username


class ReferralPost(models.Model):
    alumni = models.ForeignKey(AlumniProfile, on_delete=models.CASCADE, related_name='referrals')
    title = models.CharField(max_length=255)
    description = models.TextField()
    apply_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
