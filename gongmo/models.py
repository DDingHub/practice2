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
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=50)
    teamname = models.CharField(max_length=100,null=True)
    call = models.CharField(max_length=100,null=True)
    detail = models.TextField(null=True)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    jickgoons = models.ManyToManyField(Jickgoon) #Jickgoon 모델과의 관계를 나타냄. ManyToMany관계로써 Team객체는 여러개의 Jickgoon과 연결될 수 있다.



# class Member(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)

# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     jickgoon = models.ForeignKey('Jickgoon', on_delete=models.CASCADE,null=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     message = models.TextField(null=True) 