from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import json

class Contest(models.Model):
    title = models.CharField(max_length=255)
    photo = models.TextField()
    field = models.CharField(max_length=255)
    eligibility = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    sponsorship = models.CharField(max_length=255)
    application_period = models.CharField(max_length=255)
    prize_total = models.CharField(max_length=255)
    prize_first = models.CharField(max_length=255)
    website = models.URLField()
    details = models.TextField()
    isSchool = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True, null=True)
    viewCount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=50)
    teamname = models.CharField(max_length=100,null=True)
    call = models.CharField(max_length=100,null=True)
    detail = models.TextField(null=True)
    tendency = models.TextField(default="[]", null= True)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dev_capacity = models.PositiveIntegerField(default=0)
    plan_capacity = models.PositiveIntegerField(default=0)
    design_capacity = models.PositiveIntegerField(default=0)
    dev = models.PositiveIntegerField(default=0)
    plan = models.PositiveIntegerField(default=0)
    design = models.PositiveIntegerField(default=0)
    jickgoon_type = models.CharField(max_length=50, blank=True, choices=[('dev', '개발'), ('plan', '기획'), ('design', '디자인')])
    
    def get_tendency_as_list(self):
        return json.loads(self.tendency)

class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name = "members")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jickgoon = models.CharField(max_length=50, choices=[('dev', '개발'), ('plan', '기획'), ('design', '디자인')])

class Application(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    jickgoon = models.CharField(max_length=50, choices=[('dev', '개발'), ('plan', '기획'), ('design', '디자인')])
    is_approved = models.BooleanField(default=False)

class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta: unique_together = ['user','contest']

class Jjim(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta: unique_together = ['user','team']

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    message = models.TextField(null=True)
    is_read = models.BooleanField(default=False)

class UserInfo(models.Model):
    JICKGOON_CHOICES = [
        ('개발', '개발'),
        ('기획', '기획'),
        ('디자인', '디자인'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jickgoon_type = models.CharField(max_length=50, choices=JICKGOON_CHOICES)
    hobbies = models.JSONField(default=list)  
    courses = models.JSONField(default=list) 
    workingTimes = models.JSONField(default=list)  
    characters = models.JSONField(default=list)  
    mbti = models.JSONField(default=list)


