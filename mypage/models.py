from django.db import models
from django.contrib.auth.models import User  # 필요한 경우 임포트

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # 예시 필드, 필요한 필드들을 추가해주세요
    # 다른 필드들을 추가할 수 있습니다

    def __str__(self):
        return self.user.username

