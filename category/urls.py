from django.urls import path, re_path

from .views import (
	ElectronicsView,
	WomenView,
	MenView,
	GroceryView,
	BeautyView,
	CHomeView,
	FashionView,
	)

urlpatterns = [
	re_path(r"^electronics[0-9A-Za-z_\-]{25}/$", ElectronicsView.as_view(), name='category-electronics'),
	re_path(r"^women[0-9A-Za-z_\-]{25}/$", WomenView.as_view(), name='category-women'),
	re_path(r"^men[0-9A-Za-z_\-]{25}/$", MenView.as_view(), name='category-men'),
	re_path(r"^grocery[0-9A-Za-z_\-]{25}/$", GroceryView.as_view(), name='category-grocery'),
	re_path(r"^beauty[0-9A-Za-z_\-]{25}/$", BeautyView.as_view(), name='category-beauty'),
	re_path(r"^home[0-9A-Za-z_\-]{25}/$", CHomeView.as_view(), name='category-home'),
	re_path(r"^fashion[0-9A-Za-z_\-]{25}/$", FashionView.as_view(), name='category-fashion'),
]

