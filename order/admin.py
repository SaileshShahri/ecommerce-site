from django.contrib import admin

# Register your models here.
from .models import Order, OrderProduct

admin.site.register(Order)
admin.site.register(OrderProduct)
# admin.site.register(OrderVariant)