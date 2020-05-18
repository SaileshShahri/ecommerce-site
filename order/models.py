from django.conf import settings
from django.db import models
from django.urls import reverse
User = settings.AUTH_USER_MODEL

from django.utils import timezone
from product.models import Product, ProductVariant
from address.models import Address
# from payment.models import Payment
from django.db.models.signals import pre_save, post_save
from main.utils import unique_order_id_generator, unique_key_generator

PAYMENT_CHOICES = (
		("Pay on Delivery", "Pay on Delivery"),
		("Debit Card", "Debit Card"),
		("Credit Card", "Credit Card"),
		("Net Banking", "Net Banking"),
	)

class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.ForeignKey(Address, on_delete=models.CASCADE)
	payment = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
	order_date = models.DateTimeField(auto_now_add=True)
	order_id = models.SlugField(null=True, blank=True, unique=True) 
	confirmed = models.BooleanField(default=False) # Seller confirmation

	class Meta:
		ordering = ["-order_date"]

	def get_absolute_url(self):
		return reverse('order-detail', kwargs={"order_id": self.order_id})


def order_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.order_id:
		instance.order_id = unique_order_id_generator(instance)

pre_save.connect(order_pre_save_receiver, sender=Order)



QUANTITY_CHOICES = (
		("1", "1"),
		("2", "2"),
		("3", "3"),
		("4", "4"),
		("5", "5"),
		("6", "6"),
		("7", "7"),
		("8", "8"),
		("9", "9"),
		("10", "10"),
	)

class OrderProduct(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True, blank=True)
	quantity = models.CharField(default="1", choices=QUANTITY_CHOICES, max_length=2)
	slug = models.SlugField(null=True, blank=True, unique=True) 

	def get_seller_absolute_url(self):
		return reverse('seller-order-detail', kwargs={"slug": self.slug})


def order_product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_key_generator(instance)

pre_save.connect(order_product_pre_save_receiver, sender=OrderProduct)
