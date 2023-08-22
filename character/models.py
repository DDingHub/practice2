from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    nickname = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255)
    type_src = models.TextField()
    type_message = models.TextField()
    type_hashtag = models.TextField()
    type_explain1 = models.TextField()
    type_explain2 = models.TextField()
    type_explain3 = models.TextField()
    type_explain4 = models.TextField()
    type_best = models.CharField(max_length=255)
    type_best_message = models.TextField()
    type_best_src = models.TextField()
    type_worst = models.CharField(max_length=255)
    type_worst_message = models.TextField()
    type_worst_src = models.TextField()
    # typeId = models.IntegerField(null=True)

class MyCharacter(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name = "r_myCharacter")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
