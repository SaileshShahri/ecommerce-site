from django.urls import path, re_path

from .views import (
	BagListView,
	)

urlpatterns = [
	path("", BagListView.as_view(), name='bag-list'),
]