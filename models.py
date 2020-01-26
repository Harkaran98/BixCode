from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=20)
    year = models.CharField(max_length=5)

    def __str__(self):
        return self.make
