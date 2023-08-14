from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    name = models.CharField(max_length=100) #이름
    department = models.CharField(max_length=100) #학과
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True) # 프로필 사진
    job_title = models.CharField(max_length=100) #직군
    programming_languages = models.TextField()  # 여러 프로그래밍 언어를 입력받기 위해 TextField 사용
    contact_info = models.CharField(max_length=200) #연락수단
    introduction = models.TextField() #소개글
    portfolio = models.URLField(blank=True) #포트폴리오

    def __str__(self):
        return self.name