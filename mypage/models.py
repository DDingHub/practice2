from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    nickname = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    job = models.JSONField(null=True, blank=True)
    hobby = models.JSONField(null=True, blank=True)
    dream = models.JSONField(null=True, blank=True)
    tendency_worktime = models.CharField(max_length=100)
    tendency_personality = models.JSONField(null=True, blank=True)
    tendency_MBTI = models.CharField(max_length=10)
    languages_tools = models.JSONField(null=True, blank=True)
    call = models.JSONField(null=True, blank=True, default=dict)
    introduce = models.JSONField(null=True, blank=True, default=dict)
    portfolio = models.JSONField(null=True, blank=True, default=dict)
    user_type = models.JSONField(null=True, blank=True, default=dict)
    type_message = models.JSONField(null=True, blank=True, default=dict)

    def __str__(self):
        return self.user.username

