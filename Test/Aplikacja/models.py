from __future__ import unicode_literals
from django.db import models

class Urzadzenie(models.Model):
    Nazwa = models.CharField(max_length = 30)
    RodzajPlatformy = models.CharField(max_length=30)
    AdresIP = models.CharField(max_length=15)
    Prywatnosc = models.BooleanField()
    Stan = models.BooleanField()

    def __str__(self):
        return self.Nazwa

    class Meta:
        verbose_name_plural = 'Urzadzenie'