from django.db import models


class Kind(models.Model):
    name = models.CharField(max_length=50, verbose_name='Назва')
    description = models.CharField(max_length=500, verbose_name='Опис')

    class Meta:
        verbose_name = 'Каталог продукту'
        verbose_name_plural = 'Каталоги продуктів'

    def __str__(self):
        return self.name


class Product(models.Model):
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE, verbose_name='Продукт', related_name='RelProduct')
    name = models.CharField(max_length=50, verbose_name='Назва')
    mass = models.IntegerField(verbose_name='Масса в грамах')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    description = models.CharField(max_length=500, verbose_name='Опис')
    image = models.ImageField()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукт'
        ordering = ['kind']

    def __str__(self):
        return self.name

