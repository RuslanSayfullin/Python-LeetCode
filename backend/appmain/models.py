from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Manufacturer(models.Model):
    """Модель, описывающий производителя приборов"""
    name = models.CharField(max_length=250, verbose_name="Название компании")
    title = models.CharField(max_length=250, verbose_name="Информация о компаний")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.title


class MeasuringInstrument(models.Model):
    """Модель, описывающий измерительный прибор"""
    TYPE_CHOICES = (
        ('flow meter', 'Flow meter'),
        ('gas analyzers', 'Gas analyzers'),
    )
    name = models.CharField(max_length=250, verbose_name="Название прибора")
    title = models.CharField(max_length=250, verbose_name="Описание измерительного прибора")
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='flow meter')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Производитель прибора")
    slug = models.SlugField(max_length=250, unique_for_date='publish')   # это поле будет использоваться для формирования URL’ов
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instrument')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.title


