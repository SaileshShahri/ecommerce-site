from django.shortcuts import render
from django.views.generic import View

from product.models import Product
from category.models import Category

class ElectronicsView(View):
	template_name = "category/electronics.html"
	queryset = Product.objects.all()

	def get(self, request, *args, **kwargs):
		cobj = Category.objects.get(name="Electronics")
		obj = self.queryset.filter(category=cobj).distinct()
		context = {
		"obj" : obj,
		"cobj" : cobj,
		}
		return render(request, self.template_name, context)

class WomenView(View):
	template_name = "category/women.html"
	queryset = Product.objects.all()

	def get(self, request, *args, **kwargs):
		cobj = Category.objects.get(name="Women")
		obj = self.queryset.filter(category=cobj).distinct()
		context = {
		"obj" : obj,
		"cobj" : cobj,
		}
		return render(request, self.template_name, context)


class MenView(View):
	template_name = "category/men.html"
	queryset = Product.objects.all()

	def get(self, request, *args, **kwargs):
		cobj = Category.objects.get(name="Men")
		obj = self.queryset.filter(category=cobj).distinct()
		context = {
		"obj" : obj,
		"cobj" : cobj,
		}
		return render(request, self.template_name, context)


class GroceryView(View):
	template_name = "category/grocery.html"
	queryset = Product.objects.all()

	def get(self, request, *args, **kwargs):
		cobj = Category.objects.get(name="Grocery")
		obj = self.queryset.filter(category=cobj).distinct()
		context = {
		"obj" : obj,
		"cobj" : cobj,
		}
		return render(request, self.template_name, context)


class BeautyView(View):
	template_name = "category/beauty.html"
	queryset = Product.objects.all()

	def get(self, request, *args, **kwargs):
		cobj = Category.objects.get(name="Beauty")
		obj = self.queryset.filter(category=cobj).distinct()
		context = {
		"obj" : obj,
		"cobj" : cobj,
		}
		return render(request, self.template_name, context)


class CHomeView(View):
	template_name = "category/home.html"
	queryset = Product.objects.all()

	def get(self, request, *args, **kwargs):
		cobj = Category.objects.get(name="Home")
		obj = self.queryset.filter(category=cobj).distinct()
		context = {
		"obj" : obj,
		"cobj" : cobj,
		}
		return render(request, self.template_name, context)


class FashionView(View):
	template_name = "category/fashion.html"
	queryset = Product.objects.all()

	def get(self, request, *args, **kwargs):
		cobj = Category.objects.get(name="Fashion")
		obj = self.queryset.filter(category=cobj).distinct()
		context = {
		"obj" : obj,
		"cobj" : cobj,
		}
		return render(request, self.template_name, context)

