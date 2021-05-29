from django.db import models


class Excursion(models.Model):
    name = models.TextField(primary_key=True)
    image_link = models.TextField()
    datetime = models.TextField()
    free_places = models.IntegerField()
    description = models.TextField()
