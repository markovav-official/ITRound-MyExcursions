from django.db import models


class Excursion(models.Model):
    name = models.TextField()
    image_link = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    free_places = models.IntegerField()
