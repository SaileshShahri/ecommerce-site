# from django.conf import settings 
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory


from .models import (
        Product,
        ProductVariant,
    )

from .forms import (
    ProductForm,
    ProductVarForm,
    ProductVariantForm,
)

class ProductListView(ListView):
    template_name = 'product/list.html' #
    queryset = Product.objects.all()  #

    def get(self, request, slug=None, *args, **kwargs):
        obj = self.queryset.distinct()
        context = { 
        'productlist' : obj,
        }
        return render(request, self.template_name, context) 

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html' 
    vqueryset = ProductVariant.objects.all()

    def get(self, request, slug=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        user = self.request.user
        if slug is not None:
            instance = Product.objects.get(slug=slug)
            vaobj = self.vqueryset.filter(product=instance).distinct()
            siobj = Product.objects.filter(keyword__icontains=instance.keyword).distinct()
            context = {
            'object' : instance,
            'vaobj' : vaobj,
            "siobj" : siobj,
            }
        return render(request, self.template_name, context)

