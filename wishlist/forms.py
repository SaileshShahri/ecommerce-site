from django import forms 

from .models import WishlistProduct, Wishlist

class WishlistForm(forms.ModelForm):

	class Meta:
		model = Wishlist
		fields = [
			"title",
		]

class WishlistProductForm(forms.ModelForm):

	class Meta:
		model = WishlistProduct
		fields = [
			"wishlist",
		]
