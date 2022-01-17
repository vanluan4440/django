from django.db import models
from django.db.models.base import Model



# Create your models here.
class lesson(models.Model):
    title = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    file = models.FileField()
    quiz = models.JSONField(encoder=None)
    create_on = models.DateField()
    create_by = models.IntegerField()