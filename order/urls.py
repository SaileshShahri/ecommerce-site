from django.urls import path, re_path

from .views import (
		OrderDetailView,
		OrderPayView,
	)

urlpatterns = [
	re_path(r'^o[0-9A-Za-z_\-]{25}/(?P<order_id>[\w-]+)[0-9A-Za-z_\-]{25}/$', OrderDetailView.as_view(), name='order-detail'),
	re_path(r'^o[0-9A-Za-z_\-]{25}/pay[0-9A-Za-z_\-]{25}/(?P<order_id>[\w-]+)/$', OrderPayView.as_view(), name='order-pay'),
]