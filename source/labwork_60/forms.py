from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


class ProductForm(forms.Form):
    CHOICES = (
        ('other', 'Разное'),
        ('beverages', 'Напитки'),
        ('seeds', 'семечки'),
        ('beer', 'пиво')
    )
    title = forms.CharField(max_length=30, required=True, label='Наименование товара')
    description = forms.CharField(max_length=2000, required=False, label='Описание товара', widget=widgets.Textarea)
    image = forms.CharField(required=True, label='url фотографии', widget=widgets.URLInput)
    category = forms.ChoiceField(required=True, widget=widgets.Select, choices=CHOICES, label='Категория')
    amount = forms.IntegerField(max_value=10000, min_value=0, required=True, label='Количество')
    price = forms.DecimalField(max_value=100000, min_value=0, max_digits=7, decimal_places=2, required=True,
                               label='Цена')
