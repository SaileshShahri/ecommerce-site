from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

# from .models import Payment 
# from .forms import PaymentForm
"""
class PaymentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'payment/create.html'

    def get(self, request, *args, **kwargs):
        form = PaymentForm()  
        context = {
        'form' :  form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = PaymentForm(request.POST or None) 
        user = self.request.user
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect("/") 
            context = {
            'form' : myform 
            }
        context = { 'form' : form }
        return render(request, self.template_name, context)
"""

class OrderThankYouView(LoginRequiredMixin, View):
    template_name = "payment/thankyou.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
