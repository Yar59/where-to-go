from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Описание', blank=True)
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(
        'Картинки',
        null=True,
        blank=True,
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='images'
    )

    def __str__(self):
        return f'{self.id} {self.place.title} '
