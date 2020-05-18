from django.urls import path, re_path

from .views import (
			AddressCreateView,
			AddressUpdateView,
			AddressDeleteView,
			AddressListView,
		)

urlpatterns = [
	re_path(r'^add[0-9A-Za-z_\-]{25}/$', AddressCreateView.as_view(), name="address-add"),
	path('', AddressListView.as_view(), name="address-list"),
	re_path(r'^a[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/edit[0-9A-Za-z_\-]{25}/$', AddressUpdateView.as_view(), name="address-edit"),
	re_path(r'^a[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/delete[0-9A-Za-z_\-]{25}/$', AddressDeleteView.as_view(), name="address-delete"),
]