from django.db import models

class Game(models.Model):
    player = models.CharField(max_length=50)
    timestamp = models.DateTimeField(blank=True,null=True)
    answer1 = models.CharField(max_length=10,blank=True,null=True)
    answers2 = models.CharField(max_length=50,blank=True,null=True)
