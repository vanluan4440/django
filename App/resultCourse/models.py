from django.db import models

# Create your models here.
class resultCourse(models.Model):
    userid = models.IntegerField()
    courseid = models.IntegerField()
    point =  models.IntegerField()
    date = models.DateField()