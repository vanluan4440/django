from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class quiz(models.Model):
    question = models.CharField(max_length=255)
    type = models.CharField(max_length=255, default='radio')
    answer = models.JSONField(encoder=None)
    point = models.IntegerField()
    Rightanswer =  models.CharField(max_length=255)
    
    

