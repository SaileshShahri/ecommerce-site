from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Wishlist, WishlistProduct
from .forms import WishlistForm, WishlistProductForm
from product.models import Product

class WishlistListView(LoginRequiredMixin, ListView):
	template_name = 'wishlist/list.html' #
	queryset = Wishlist.objects.all()  #

	def get(self, request, *args, **kwargs):
		user = self.request.user
		obj = self.queryset.filter(user=user).order_by("-timestamp").distinct()
		context = { 'wishlist' : obj } #
		return render(request, self.template_name, context) 
    

class WishlistProductCreateView(LoginRequiredMixin, CreateView):
	template_name = 'wishlist/create.html'

	def get(self, request, slug=None, *args, **kwargs):
		user = self.request.user 
		slug = self.kwargs.get("slug")
		if slug is not None:
			obj = Product.objects.get(slug=slug)
			form = WishlistProductForm()
			form.fields["wishlist"].queryset = Wishlist.objects.filter(user=user).distinct()
			context = {
			"form" : form,
			"obj" : obj,
			}
			return render(request, self.template_name, context)
		return render(request, "400.html", {})

	def post(self, request, slug=None, *args, **kwargs):
		slug = self.kwargs.get("slug")
		user = self.request.user
		if slug is not None:
			obj = Product.objects.get(slug=slug)
			if obj is not None:
				form = WishlistProductForm(request.POST or None)
				if form.is_valid():
					myform = form.save(commit=False)
					myform.product = obj
					myform.save()
					return redirect("product-detail", slug=slug)
					context = {
					"form" : myform,
					}
					return render(request, self.template_name, context)
				return render(request, "400.html", {})
			return render(request, "400.html", {})
		return render(request, "400.html", {})


class WishlistCreateView(LoginRequiredMixin, CreateView):
	template_name = "wishlist/wish.html"

	def get(self, request, *args, **kwargs):
		user = self.request.user
		form = WishlistForm()
		context = {
		"form" : form, 
		}
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		user = self.request.user
		form = WishlistForm(request.POST or None)
		if form.is_valid():
			myform = form.save(commit=False)
			myform.user = user
			myform.save()
			return redirect("wishlist")
			context = {
			'form' : myform, 
			}
			return render(request, self.template_name, context)
		return render(request, "400.html", {})


class WishlistDetailView(LoginRequiredMixin, DetailView):
	template_name = 'wishlist/detail.html'

	def get(self, request, slug=None, *args, **kwargs):
		slug = self.kwargs.get("slug")
		user = self.request.user
		if slug is not None:
			wishlist = Wishlist.objects.get(slug=slug)
			if wishlist.user == user:
				wobj = WishlistProduct.objects.filter(wishlist=wishlist)
				context = {
				"wishlist" : wishlist,
				"wobj" : wobj,
				}
				return render(request, self.template_name, context)
			return render(request, "400.html", {})
		return render(request, "400.html", {})

class WishlistDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'wishlist/delete.html' 

    def get(self, request, slug=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        user = self.request.user
        if slug is not None:
            obj = Wishlist.objects.get(slug=slug)
            if obj is not None:
                if obj.user == user:
                    context = {
                    "obj" : obj,
                    }
                    return render(request, self.template_name, context)
                return render(request, "400.html", {})
            return render(request, "400.html", {})
        return render(request, "400.html", {})

    def post(self, request, slug=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        if slug is not None:
            obj = Wishlist.objects.get(slug=slug)
            if obj is not None:
                obj.delete()
                return redirect('wishlist')
                return render(request, self.template_name, {})
            return render(request, "400.html", {})
        return render(request, "400.html", {})


class WishlistView(LoginRequiredMixin, View):
	def get(self, request, slug=None, *args, **kwargs):
		user = self.request.user 
		if user is not None:
			wishlist = Wishlist.objects.filter(user=user).distinct()
			if not wishlist:
				return redirect('wishlist-pro-create', slug=slug)
			else:
				return redirect('wishlist-product-create', slug=slug)


class WishlistProCreateView(LoginRequiredMixin, CreateView):
	template_name = "wishlist/wish.html"

	def get(self, request, slug=None, *args, **kwargs):
		user = self.request.user
		slug = self.kwargs.get("slug")
		if slug is not None:
			obj = Product.objects.get(slug=slug)
			form = WishlistForm()
			context = {
			"form" : form,
			"obj" : obj,
			}
			return render(request, self.template_name, context)
		return render(request, "400.html", {})

	def post(self, request, slug=None, *args, **kwargs):
		slug = self.kwargs.get("slug")
		user = self.request.user
		if slug is not None:
			obj = Product.objects.get(slug=slug)
			if obj is not None:
				form = WishlistForm(request.POST or None)
				if form.is_valid():
					myform = form.save(commit=False)
					myform.user = user
					myform.save()
					WishlistProduct.objects.create(wishlist=myform, product=obj)
					return redirect("product-detail", slug=slug)
					context = {
					"form" : myform,
					}
					return render(request, self.template_name, context)
				return render(request, "400.html", {})
			return render(request, "400.html", {})
		return render(request, "400.html", {})

