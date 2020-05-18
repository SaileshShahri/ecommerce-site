from django import forms
from address.models import Address
from .models import Order, OrderProduct

class OrderForm(forms.ModelForm):

	class Meta:
		model = Order
		fields = [
				'address',
				'payment',
			]

class OrderProductForm(forms.ModelForm):

	class Meta:
		model = OrderProduct
		fields = [
			'quantity',
		]
