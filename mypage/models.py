from django.db import models
from django.contrib.auth.models import User  # 필요한 경우 임포트

class UserProfile(models.Model):
    class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    # ... 나머지 필드들 ...

    def __str__(self):
        return self.user.username

