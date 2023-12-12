from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    short_description = models.TextField(
        verbose_name='Краткое описание',
        blank=True)
    long_description = HTMLField(verbose_name='Полное описание', blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['title']

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='images')
    position = models.PositiveIntegerField(
        verbose_name='Позиция',
        default=0,
        blank=False,
        null=False,
        db_index=True)

    class Meta:
        ordering = ['position']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
