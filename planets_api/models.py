from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField(null=True)

    terrains = models.ManyToManyField("Terrain", blank=True)
    climates = models.ManyToManyField("Climate", blank=True)

    def __str__(self):
        return self.name


class Terrain(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Climate(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
