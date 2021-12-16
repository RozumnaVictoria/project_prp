from django.db import models


class Contacts(models.Model):
    address = models.CharField(max_length=50, verbose_name='Адрес')
    number_tel = models.IntegerField(verbose_name='Номер телефону')
    email = models.EmailField(verbose_name='Пошта')
    schedule = models.TextField(verbose_name="Графік роботи")

    class Meta:
        verbose_name = "Котактні дані"
        verbose_name_plural = "Котактні дані"

    def __str__(self):
        return "Контакти"
