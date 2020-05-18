from django.urls import path, re_path

from .views import (
		ProductDetailView,
		ProductListView,
	)

from bag.views import (
		BagCreateView,
		BagProductCreateView,
		BagVariantCreateView,
		BagVariantSelectListView,
	)
from wishlist.views import WishlistProductCreateView, WishlistView
from order.views import (
	BuyNowCreateView, 
	OrderProductCreateView, 
	OrderVariantCreateView,
	VariantSelectListView,
	)


urlpatterns = [
	# product 
	re_path(r'^p[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/$', ProductDetailView.as_view(), name='product-detail'),
	path('', ProductListView.as_view(), name='product-list'),

	# bag 
	re_path(r"^p[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/bag/$", BagCreateView.as_view(), name='bag-create'),
	re_path(r"^p[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/bag[0-9A-Za-z_\-]{25}/product[0-9A-Za-z_\-]{25}/$", BagProductCreateView.as_view(), name='bag-create-product'),
	re_path(r"^p[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/bag[0-9A-Za-z_\-]{25}/select[0-9A-Za-z_\-]{25}/$", BagVariantSelectListView.as_view(), name='bag-create-select'),
	re_path(r"^p[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/bag[0-9A-Za-z_\-]{25}/variant[0-9A-Za-z_\-]{25}/$", BagVariantCreateView.as_view(), name='bag-create-variant'),

	# order
	re_path(r"^p[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/buy/$", BuyNowCreateView.as_view(), name='buy-now-create'),
	re_path(r"^p[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/buy[0-9A-Za-z_\-]{25}/product[0-9A-Za-z_\-]{25}/$", OrderProductCreateView.as_view(), name='order-product-create'),
	re_path(r"^p[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/buy[0-9A-Za-z_\-]{25}/select[0-9A-Za-z_\-]{25}/$", VariantSelectListView.as_view(), name='order-variant-select'),
	re_path(r"^p[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/buy[0-9A-Za-z_\-]{25}/variant[0-9A-Za-z_\-]{25}/$", OrderVariantCreateView.as_view(), name='order-variant-create'),

	# Wishlist 
	re_path(r'^p[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/wishlist/$', WishlistView.as_view(), name='wishlist-redirect'),
	re_path(r'^p[0-9A-Za-z_\-]{25}/(?P<slug>[\w-]+)[0-9A-Za-z_\-]{25}/wishlist/product/$', WishlistProductCreateView.as_view(), name='wishlist-product-create'),
]