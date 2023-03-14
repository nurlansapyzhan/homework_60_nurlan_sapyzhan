from django import forms
from django.core.exceptions import ValidationError

from labwork_60.models import Product, Order


def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError('Phone number should contain only digits')


class ProductForm(forms.ModelForm):
    CHOICES = (
        ('other', 'Разное'),
        ('beverages', 'Напитки'),
        ('seeds', 'семечки'),
        ('beer', 'пиво')
    )
    category = forms.ChoiceField(choices=CHOICES, initial='other', label='Category')

    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'category', 'amount', 'price')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image URL',
            'category': 'Category',
            'amount': 'Amount',
            'price': 'Price'
        }
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'int_input', 'min': 0}),
            'price': forms.NumberInput(attrs={'class': 'int_input', 'min': 0})
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label='Search')


class OrderForm(forms.ModelForm):
    phone_number = forms.CharField(validators=[validate_phone_number],
                                   widget=forms.TextInput(attrs={'placeholder': '87771231212'}))

    class Meta:
        model = Order
        fields = ('username', 'address', 'phone_number')
        labels = {
            'username': 'Username',
            'address': 'Address',
            'phone_number': 'Phone number'
        }
