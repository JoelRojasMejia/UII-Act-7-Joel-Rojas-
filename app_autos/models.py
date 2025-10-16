from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.año})'
