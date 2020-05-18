from django import forms

from .models import (
		Product,
		ProductVariant,
	)

class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = [
				'image',
				'title',
				'category',
				'categorytype',
				'price',
				'comparedprice',
				'quantity',
				'description',
				'keyword',
			]


class ProductVarForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = [
			'variants_type',
		]


class ProductVariantForm(forms.ModelForm):

	class Meta:
		model = ProductVariant
		fields = [
		'desc',
		'price',
		'comparedprice',
		'quantity',
		]
