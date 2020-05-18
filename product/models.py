import datetime 
import random 
import os 

from django.conf import settings 
from django.db import models

User = settings.AUTH_USER_MODEL

from category.models import Category
from django.urls import reverse
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from main.utils import unique_slug_generator, get_filename, unique_key_generator

VARIANTS_TYPE = (
			("Size", "Size"),
			("Colour", "Colour"),
			("Material", "Material"),
			("Style", "Style"),
			("Other", "Other"),
		)

def get_filename(path):
    return os.path.basename(path)

def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "productimg/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )


class ProductQuerySet(models.query.QuerySet):
	def search(self, query):
		lookup = (
				# Q(seller__icontains=query) |
				# Q(category__icontains=query) |
				Q(title__icontains=query) |
				Q(keyword__icontains=query) 
			)
		return self.filter(lookup).distinct()


class ProductManager(models.Manager):
	def get_queryset(self, *args, **kwargs):
		return ProductQuerySet(self.model, using=self.db, *args, **kwargs)

	def search(self, query):
		return self.get_queryset().search(query)


class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	categorytype = models.CharField(max_length=300, blank=True)
	title = models.CharField(max_length=140)
	image = models.ImageField(upload_to=upload_image_path, null=True)
	price = models.DecimalField(max_digits=20, decimal_places=2)
	comparedprice = models.DecimalField(max_digits=20, decimal_places=2)
	quantity = models.DecimalField(max_digits=20, decimal_places=0)
	description = models.TextField(max_length=1000)
	keyword = models.TextField(max_length=500)
	slug = models.SlugField(null=True, blank=True, unique=True, max_length=140) 
	variants_type = models.CharField(max_length=18, choices=VARIANTS_TYPE, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = ProductManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("product-detail", kwargs={"slug": self.slug})

	def get_seller_absolute_url(self):
		return reverse("seller-product-detail", kwargs={"slug": self.slug})

	def get_buy_now_create_url(self):
		return reverse("buy-now-create", kwargs={"slug": self.slug})


def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)


class ProductVariant(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	desc = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=20, decimal_places=2)
	comparedprice = models.DecimalField(max_digits=20, decimal_places=2)
	quantity = models.IntegerField()
	slug = models.SlugField(null=True, blank=True, unique=True) 

	def get_absolute_url(self):
		return reverse("seller-product-variant-edit", kwargs={"slug" : self.slug})

	def get_delete_url(self):
		return reverse("seller-product-variant-delete", kwargs={"slug" : self.slug})

	def get_order_url(self):
		return reverse("order-variant-create", kwargs={"slug" : self.slug})

	def get_bag_url(self):
		return reverse("bag-create-variant", kwargs={"slug" : self.slug})


def product_variant_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_key_generator(instance)

pre_save.connect(product_variant_pre_save_receiver, sender=ProductVariant)
