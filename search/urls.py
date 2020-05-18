from django.urls import path, re_path

from .views import (
		productsearchview,
	)

urlpatterns = [
	path('product/', productsearchview, name='search'),
]
