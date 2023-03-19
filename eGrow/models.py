from django.db import models

# Create your models here.


class Test(models.Model):
    id = models.IntegerField()
    nombre = models.CharField(max_length=200)