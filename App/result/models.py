from django.db import models

# Create your models here.
class result(models.Model):
    userid = models.IntegerField()
    lessonid = models.IntegerField()
    point =  models.IntegerField()
    date = models.DateField()