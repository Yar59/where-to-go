from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Описание', blank=True)
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')
    place_id = models.CharField('ID места', max_length=200, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


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
    ordinal_number = models.PositiveIntegerField(
        'Порядковый номер',
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    def __str__(self):
        return f'{self.id} {self.place.title} '

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['ordinal_number']
