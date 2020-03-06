from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, default='名前')
    age = models.IntegerField(default=20)
    gender = models.CharField(max_length=10, default='')
    def __str__(self):
        return self.username

class Event(models.Model):

    event_name = models.CharField(max_length=100, default='タイトル')
    place = models.CharField(max_length=100, default='地域を選ぼう', null=True)
    help = models.CharField(max_length=200, default='手伝いを書こう')
    parttime = models.IntegerField(default=0)
    join = models.IntegerField(default=0)
    planning_number = models.IntegerField(default=0)
    thanks = models.CharField(max_length=200, default='地域体験を書こう')
    user = models.ForeignKey(User,null=True, on_delete=DO_NOTHING)

    def __str__(self):
        return self.event_name
# Create your models here.
