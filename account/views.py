from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth import views as django_views

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.tokens import default_token_generator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy
from django.utils.translation import pgettext, ugettext_lazy as _
from django.views.decorators.http import require_POST

from django.views.generic import UpdateView, View

from .forms import (
    PasswordResetForm,
    SignupForm,
    UserForm,
    LoginForm,
)

from .models import User


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = auth.authenticate(request=request, email=email, password=password)
        if user:
            auth.login(request, user)
        return redirect('home')
    ctx = {"form": form}
    return TemplateResponse(request, "account/signup.html", ctx)

def login(request):
	kwargs = {"template_name": "account/login.html", "authentication_form": LoginForm}
	return django_views.LoginView.as_view(**kwargs)(request, **kwargs)

def password_reset(request):
    kwargs = {
        "template_name": "account/password_reset.html",
        "success_url": reverse_lazy("reset-password-done"),
        "form_class": PasswordResetForm,
    }
    return django_views.PasswordResetView.as_view(**kwargs)(request, **kwargs)

class ProfileView(LoginRequiredMixin, View):
    template_name = "account/profile.html"

    def get(self, request, *args, **kwargs):
        user = self.request.user 
        obj = None
        context = {}
        if user is not None:
            obj = User.objects.get(id=user.id)
            context = {
                'object' : obj,
            }
            return render(request, self.template_name, context)
        else:
            return render(request, "400.html", {})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'account/profile_edit.html'
    queryset = User.objects.all()

    def get_object(self):
        user = self.request.user
        obj = None
        if user is not None:
            obj = User.objects.get(id=user.id)
        return obj

    def get(self, request, pk=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            if obj == request.user:
                form = UserForm(instance=obj)
                context = {
                	'object' : obj,
	                'form' : form,
	               } 
                return render(request, self.template_name, context)
            return render(request, "400.html", context)

    def post(self, request, pk=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = UserForm(request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form.save()
                return redirect("accountprofile") 
                context = {
    	        	'object' : obj,
        	    	'form' : form,
            	}
            return render(request, self.template_name, context)
