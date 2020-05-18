from django.urls import path, re_path

from .views import (
		# PaymentCreateView,
		OrderThankYouView,
	)

urlpatterns = [
	# path('', PaymentCreateView.as_view(), name='payment-create'),
	re_path(r'^thankyou[0-9A-Za-z_\-]{25}/$', OrderThankYouView.as_view(), name='order-thankyou'),
]