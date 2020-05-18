from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Address 
from .forms import AddressForm


class AddressListView(LoginRequiredMixin, ListView):
    template_name = 'address/list.html'
    queryset = Address.objects.all()

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if user is not None:
            aobj = self.queryset.filter(user=user).filter(seller=False).order_by("-timestamp").distinct()
            context = {
            'aobj' : aobj,
            }
            return render(request, self.template_name, context)
        return render(request, "400.html", {})


class AddressCreateView(LoginRequiredMixin, CreateView):
    template_name = 'address/add.html'

    def get(self, request, *args, **kwargs):
        form = AddressForm()  
        context = {
        'form' :  form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = AddressForm(request.POST or None) 
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect("address-list")
            context = {
            'form' : myform 
            }
        context = { 'form' : form }
        return render(request, self.template_name, context)


class AddressUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'address/edit.html' #

    def get(self, request, slug=None, *args, **kwargs):
        user = self.request.user
        slug = self.kwargs.get("slug")
        if slug is not None:
            obj = Address.objects.get(slug=slug)
            if obj.user == user:
                form = AddressForm(instance=obj) 
                context = {
                        'object' : obj,
                        'form' : form,
                    }
                return render(request, self.template_name, context)
            return render(request, "400.html", {})
        return render(request, "400.html", {})


    def post(self, request, slug=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        if slug is not None:
            obj = Address.objects.get(slug=slug)
            form = AddressForm(request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form.save()
                return redirect("address-list") 
                context = {
                    'object' : obj,
                    'form' : form,
                }
                return render(request, self.template_name, context)
            return render(request, "400.html", {})


class AddressDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'address/delete.html' 

    def get(self, request, slug=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        user = self.request.user
        if slug is not None:
            obj = Address.objects.get(slug=slug)
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
            obj = Address.objects.get(slug=slug)
            if obj is not None:
                obj.delete()
                return redirect('address-list')
                return render(request, self.template_name, {})
            return render(request, "400.html", {})
        return render(request, "400.html", {})
