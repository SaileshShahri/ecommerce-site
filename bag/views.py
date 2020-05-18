from django.shortcuts import render, redirect 
from django.views.generic import ListView, CreateView, View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bag
from product.models import Product, ProductVariant
from order.forms import OrderForm, OrderProductForm
from order.models import Order, OrderProduct
from django.forms import modelformset_factory


class BagListView(LoginRequiredMixin, ListView):
    template_name = 'bag/list.html'
    queryset = Bag.objects.all()  

    def get(self, request, *args, **kwargs):
    	user = self.request.user
    	obj = self.queryset.filter(user=user).distinct()
    	context = { 'baglist' : obj }
    	return render(request, self.template_name, context) 


class BagCreateView(LoginRequiredMixin, CreateView):
	def get(self, request, slug=None, *args, **kwargs):
		user = self.request.user
		slug = self.kwargs.get("slug")
		if slug is not None:
			obj = Product.objects.get(slug=slug)
			if obj is not None:
				vobj = ProductVariant.objects.all().filter(product=obj)
				if not vobj:
					return redirect("bag-create-product", slug=obj.slug)
				else:
					return redirect("bag-create-select", slug=obj.slug)


class BagProductCreateView(LoginRequiredMixin, CreateView):
	def get(self, request, slug=None, *args, **kwargs):
		user = self.request.user
		slug = self.kwargs.get("slug")
		if slug is not None:
			product = Product.objects.get(slug=slug)
			obj = Bag.objects.create(user=user, product=product)
			return redirect("product-detail", slug=slug)


class BagVariantCreateView(LoginRequiredMixin, CreateView):
	def get(self, request, slug=None, *args, **kwargs):
		user = self.request.user
		slug = self.kwargs.get("slug")
		if slug is not None:
			variant = ProductVariant.objects.get(slug=slug)
			obj = Bag.objects.create(
				user=user, 
				product=variant.product, 
				variant=variant
			)
			return redirect("product-detail", slug=variant.product.slug)


class BagVariantSelectListView(LoginRequiredMixin, ListView):
    template_name = "bag/var.html"

    def get(self, request, slug=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        if slug is not None:
            product = Product.objects.get(slug=slug)
            if product is not None:
                variant = ProductVariant.objects.filter(product=product)
                context = {
                "product" : product,
                "variant" : variant,
                }
                return render(request, self.template_name, context)
            return render(request, "400.html", {})
        return render(request, "400.html", {})

