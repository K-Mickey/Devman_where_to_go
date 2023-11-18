from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
        ordering = ['title']


class Image(models.Model):
    img = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(
        verbose_name="Позиция",
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ['position']
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
