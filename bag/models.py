from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL
from product.models import Product, ProductVariant


class Bag(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
	variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
