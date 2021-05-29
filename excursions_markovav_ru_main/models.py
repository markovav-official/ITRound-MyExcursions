from django.db import models


class Excursion(models.Model):
    name_date = models.TextField(primary_key=True)
    name = models.TextField()
    image_link = models.TextField()
    datetime = models.TextField()
    free_places = models.IntegerField()
    description = models.TextField()

    def to_qr(self):
        data = [
            'Экскурсия: ' + self.name,
            'Время и дата: ' + self.datetime,
            'Запись: ' + '%reg_date%'
        ]
        return ' \n'.join(data)
