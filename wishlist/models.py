import datetime 
import random 
import os 


from django.conf import settings 
from django.db import models

User = settings.AUTH_USER_MODEL

from product.models import Product
from django.utils import timezone
from django.urls import reverse
from django.db.models.signals import pre_save, post_save

from main.utils import unique_slug_generator, get_filename


class Wishlist(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=140, default="Wishlist")
	timestamp = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(null=True, blank=True, unique=True, max_length=140) 

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("wishlist-detail", kwargs={"slug":self.slug})

	def get_delete_url(self):
		return reverse("wishlist-delete", kwargs={"slug" : self.slug})


def wishlist_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(wishlist_pre_save_receiver, sender=Wishlist) 


class WishlistProduct(models.Model):
	wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
