from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Serie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

class Episode(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    #relacion con el modelo de arriba
    serie = models.ForeignKey(Serie, on_delete=CASCADE)