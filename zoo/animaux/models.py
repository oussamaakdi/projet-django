from django.db import models


class animal(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    etat = models.CharField(max_length=100)
    lieu = models.CharField(max_length=100)
    image_url = models.URLField(default=None)

    def __str__(self):
        return self.name


class equipement(models.Model):
    name = models.CharField(max_length=100)
    disponibilite = models.CharField(max_length=100)
    image_url = models.URLField(default=None)

    def __str__(self):
        return self.name
