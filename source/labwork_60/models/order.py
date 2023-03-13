from django.core.validators import MinValueValidator
from django.db import models


class Order(models.Model):
    products = models.ManyToManyField(
        to='labwork_60.product',
        through='OrderProducts'
    )
    username = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Username'
    )
    phone_number = models.CharField(
        max_length=12,
        null=False,
        blank=False,
        verbose_name='Phone number'
    )
    address = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Address'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )


class OrderProducts(models.Model):
    product = models.ForeignKey(
        to='labwork_60.product',
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        to='labwork_60.order',
        on_delete=models.CASCADE
    )
    amount = models.IntegerField(
        verbose_name='Amount',
        validators=[MinValueValidator(1)]
    )
