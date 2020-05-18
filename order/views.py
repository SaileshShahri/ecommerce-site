from django.shortcuts import render, redirect
from django.views.generic import UpdateView, ListView, View, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderProduct
from .forms import (
    OrderForm,
    OrderProductForm,
    )
from address.forms import AddressForm
from address.models import Address
from product.models import Product, ProductVariant
from bag.models import Bag 

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order/detail.html'
    queryset = OrderProduct.objects.all()

    def get(self, request, order_id=None, *args, **kwargs):
        order_id = self.kwargs.get("order_id")
        query = None
        user = self.request.user
        if order_id is not None:
            instance = Order.objects.get(order_id=order_id)
            if instance is not None:
                if instance.user == user:
                    obj = self.queryset.filter(order=instance).distinct()
                    context = {
                    'object' : instance,
                    'obj' : obj,
                    }
                    return render(request, self.template_name, context)
                return render(request, "400.html", {})
            return render(request, "400.html", {})
        return render(request, "400.html", {})


class BuyNowCreateView(LoginRequiredMixin, CreateView):
    def get(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        user = self.request.user
        if slug is not None:
            obj = Product.objects.get(slug=slug)
            if obj is not None:
                vobj = ProductVariant.objects.all().filter(product=obj)
                if not vobj:
                    return redirect("order-product-create", slug=obj.slug)
                else:
                    return redirect("order-variant-select", slug=obj.slug)
            return render(request, "400.html", {})


class OrderProductCreateView(LoginRequiredMixin, CreateView):
    template_name = "order/product.html"

    def get(self, request, slug=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        user = self.request.user
        if slug is not None:
            product = Product.objects.get(slug=slug)
            address = Address.objects.filter(user=user).distinct()
            if product is not None:
                form = OrderForm()
                form.fields["address"].queryset = Address.objects.filter(user=user).distinct()
                pform = OrderProductForm()
                context = {
                "product" : product,
                "form" : form,
                "pform" : pform,
                "address" : address,
                }
                return render(request, self.template_name, context)
            return render(request, "400.html", {})
        return render(request, "400.html", {})

    def post(self, request, slug=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        user = self.request.user
        if slug is not None:
            if user is not None:
                product = Product.objects.get(slug=slug)
                if product is not None:
                    pform = OrderProductForm(request.POST or None)
                    form = OrderForm(request.POST or None)
                    if pform.is_valid() and form.is_valid():
                        mypform = pform.save(commit=False)
                        myform = form.save(commit=False)
                        myform.user = user
                        myform.confirmed = True
                        myform.save()
                        mypform.order = myform
                        mypform.product = product
                        mypform.save()
                        print(myform.order_id)
                        return redirect("order-pay", order_id=myform.order_id)
                        context = {
                        "product" : product,
                        "form" : myform,
                        "pform" : pform,
                        }
                        return render(request, self.template_name, context)
                    return render(request, "400.html", {})
                return render(request, "400.html", {})
            return render(request, "400.html", {})
        return render(request, "400.html", {})



class OrderVariantCreateView(LoginRequiredMixin, CreateView):
    template_name = "order/variant.html"

    def get(self, request, slug=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        user = self.request.user
        if slug is not None:
            product = ProductVariant.objects.get(slug=slug)
            if product is not None:
                form = OrderForm()
                form.fields["address"].queryset = Address.objects.filter(user=user).distinct()
                pform = OrderProductForm()
                context = {
                "variant" : product,
                "form" : form,
                "vform" : pform,
                }
                return render(request, self.template_name, context)
            return render(request, "400.html", {})
        return render(request, "400.html", {})

    def post(self, request, slug=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        user = self.request.user
        if slug is not None:
            if user is not None:
                product = ProductVariant.objects.get(slug=slug)
                if product is not None:
                    pform = OrderProductForm(request.POST or None)
                    form = OrderForm(request.POST or None)
                    if pform.is_valid() and form.is_valid():
                        mypform = pform.save(commit=False)
                        myform = form.save(commit=False)
                        myform.user = user
                        myform.confirmed = True
                        myform.save()
                        mypform.order = myform
                        mypform.variant = product
                        mypform.product = product.product
                        mypform.save()
                        return redirect("order-pay", order_id=myform.order_id)
                        context = {
                        "variant" : product,
                        "form" : myform,
                        "vform" : pform,
                        }
                        return render(request, self.template_name, context)
                    return render(request, "400.html", {})
                return render(request, "400.html", {})
            return render(request, "400.html", {})
        return render(request, "400.html", {})


class OrderPayView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        slug = self.kwargs.get("order_id")
        obj = Order.objects.get(order_id=slug)
        if obj.payment == "Pay on Delivery":
            return redirect("order-thankyou")
        else:
            return redirect("order-thankyou") # change this url 



class VariantSelectListView(LoginRequiredMixin, ListView):
    template_name = "order/var.html"

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