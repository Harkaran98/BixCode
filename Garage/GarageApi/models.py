from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=10)
    year = models.CharField(max_length=4)

