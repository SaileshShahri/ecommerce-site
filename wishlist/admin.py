from django.contrib import admin

# Register your models here.
from .models import Wishlist, WishlistProduct

admin.site.register(Wishlist)
admin.site.register(WishlistProduct)