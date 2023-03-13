from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Наименование товара'
    )
    description = models.CharField(
        max_length=2000,
        null=True,
        verbose_name='Описание товара'
    )
    image = models.TextField(
        null=False,
        verbose_name='Фото товара'
    )
    category = models.CharField(
        max_length=50,
        null=False,
        default='other',
        verbose_name='Категория'
    )
    amount = models.IntegerField(
        null=False,
        default=1,
        verbose_name='Остаток',
        validators=[MinValueValidator(0)]
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2
    )
