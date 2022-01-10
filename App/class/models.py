from django.db import models

# Create your models here.
class Class_A(models.Model):
    title = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    desc =  models.CharField(max_length=255)
    course =  models.JSONField(encoder=None)
    created_on = models.DateTimeField()
    createdBy = models.IntegerField()
