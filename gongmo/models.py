from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Contest(models.Model):
    title = models.CharField(max_length=255)
    photo = models.URLField()
    field = models.CharField(max_length=255)
    eligibility = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    sponsorship = models.CharField(max_length=255)
    application_period = models.CharField(max_length=255)
    prize_total = models.CharField(max_length=255)
    prize_first = models.CharField(max_length=255)
    website = models.URLField()
    details = models.TextField()

    def __str__(self):
        return self.title
    
class Jickgoon(models.Model):
    name = models.CharField(max_length=50)

class Team(models.Model):
    name = models.CharField(max_length=50)
    teamname = models.CharField(max_length=100,null=True)
    call = models.CharField(max_length=100,null=True)
    detail = models.TextField(null=True)
    gongmo = models.ForeignKey(Contest, on_delete=models.CASCADE)
    jickgoons = models.ManyToManyField(Jickgoon, through="Member")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dev_capacity = models.PositiveIntegerField(default=0)
    plan_capacity = models.PositiveIntegerField(default=0)
    design_capacity = models.PositiveIntegerField(default=0)
    def get_dev_capacity(self):
        return self.member_set.filter(jickgoon__name='개발').count()

    def get_plan_capacity(self):
        return self.member_set.filter(jickgoon__name='기획').count()

    def get_design_capacity(self):
        return self.member_set.filter(jickgoon__name='디자인').count()

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    jickgoon = models.ForeignKey(Jickgoon, on_delete=models.CASCADE)

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    jickgoon = models.ForeignKey('Jickgoon', on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    message = models.TextField(null=True) 