from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField(verbose_name='Картинка')
    position = models.PositiveIntegerField(default=1, verbose_name="Позиция")
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
