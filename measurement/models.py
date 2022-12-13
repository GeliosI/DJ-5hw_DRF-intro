from django.db import models

# from smart_home.settings import MEDIA_ROOT


class Sensor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['-name']

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='Датчик', related_name='measurements')
    temperature = models.IntegerField(verbose_name='Температура при измерении')
    created_at = models.DateField(verbose_name='Дата измерения', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Дата изменения', auto_now=True)
    image = models.ImageField(verbose_name='Изображение', null=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['-created_at']
