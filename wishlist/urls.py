from django.urls import path, re_path

from .views import (
	WishlistListView,
	WishlistCreateView,
	WishlistDetailView,
	WishlistDeleteView,
	WishlistProCreateView,
)


urlpatterns = [
	path('', WishlistListView.as_view(), name='wishlist'),
	re_path(r'^create[0-9A-Za-z_\-]{25}/$', WishlistCreateView.as_view(), name='wishlist-create'),
	re_path(r'^w[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/$', WishlistDetailView.as_view(), name='wishlist-detail'),
	re_path(r'^w[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/delete[0-9A-Za-z_\-]{25}/$', WishlistDeleteView.as_view(), name='wishlist-delete'),
	re_path(r'^w[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/pro[0-9A-Za-z_\-]{25}/$', WishlistProCreateView.as_view(), name='wishlist-pro-create'),
]