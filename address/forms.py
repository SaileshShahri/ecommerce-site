from django import forms

from .models import Address

class AddressForm(forms.ModelForm):

	class Meta:
		model = Address
		fields = (
				'address_type',
				'title',
				'address_line',
				'landmark',
				'area',
				'city',
				'state',
				'pincode',
			)
