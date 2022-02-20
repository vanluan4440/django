from venv import create
from django.db import models
from django.db.models.base import Model

# Create your models here.
class Exam(models.Model):
    course= models.IntegerField(default=0)
    nameExam = models.CharField(max_length=255, default='Exam')
    DateStart = models.DateField()
    EndDate = models.DateField()
    Time = models.IntegerField(default=15)
    ListQuestion = models.JSONField()
    createBy = models.CharField(max_length=255)