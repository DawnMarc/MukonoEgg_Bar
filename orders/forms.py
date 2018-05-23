from django.forms import ModelForm
from django import forms
from .models import Order, Collected


class OrderForm(ModelForm):
    OPTIONS = (
        ('',''),
        ('Cash','Cash'),
        ('MTN Mobile Money','MTN Mobile Money'),
        ('Airtel Money)', 'Airtel Money')
    )
    OPTIONS2 = (
        ('Confirm', 'Confirm'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
        ('Cancelled', 'Cancelled')
    )
    order_status = forms.TypedChoiceField(required=False, choices=OPTIONS2, widget=forms.RadioSelect)
    payment_option = forms.ChoiceField(choices=OPTIONS)

    class Meta:
        model = Order
        fields = ['name', 'phone', 'address',
                  'delivery_date', 'product_id', 'payment_option',
                  'px_per_tray', 'px_per_egg', 'no_of_trays', 'amount',
                  'order_status']
        widgets = {
            'px_per_tray': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'px_per_egg': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'product_id': forms.TextInput(attrs={'readonly': 'readonly'}),
            'delivery_date': forms.DateInput(),
        }


class CollectionForm(ModelForm):
    class Meta:
        model = Collected
        fields = ['eggs', 'trays', 'damaged', 'Date']
        widgets = {
            'eggs': forms.NumberInput(),
            'trays': forms.NumberInput(),
            'damaged':  forms.NumberInput(),
            'Date': forms.DateTimeInput()
        }
