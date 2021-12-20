from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class course(models.Model):
    title =  models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    lesson = models.JSONField(encoder=None)
    create_on = models.DateTimeField()
    create_by = models.CharField(max_length=255)