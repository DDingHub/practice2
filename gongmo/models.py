from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=50)
    teamname = models.CharField(max_length=100,null=True)
    call = models.CharField(max_length=100,null=True)
    detail = models.TextField(null=True)
    tendency = models.JSONField(default = list)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dev_capacity = models.PositiveIntegerField(default=0)
    plan_capacity = models.PositiveIntegerField(default=0)
    design_capacity = models.PositiveIntegerField(default=0)
    dev = models.PositiveIntegerField(default=0)
    plan = models.PositiveIntegerField(default=0)
    design = models.PositiveIntegerField(default=0)
    jickgoon_type = models.CharField(max_length=50, blank=True, choices=[('dev', '개발'), ('plan', '기획'), ('design', '디자인')])


class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name = "members")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jickgoon = models.CharField(max_length=50, choices=[('dev', '개발'), ('plan', '기획'), ('design', '디자인')])

class Application(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    jickgoon = models.CharField(max_length=50, choices=[('dev', '개발'), ('plan', '기획'), ('design', '디자인')])
    is_approved = models.BooleanField(default=False)