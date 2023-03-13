from django import forms

from labwork_60.models import Product


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
