from django.db import models


class Promotions(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва акції')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.CharField(max_length=500, blank=True, verbose_name='Опис')
    end = models.CharField(max_length=100, blank=True, verbose_name='Кінець акції')
    image = models.ImageField(upload_to='images', verbose_name='Обрати фото')

    class Meta:
        verbose_name = 'Акція'
        verbose_name_plural = 'Акції'

    def __str__(self):
        return self.name

