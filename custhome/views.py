from django.shortcuts import render
from django.views.generic import View, ListView


class HomeMainView(View):
    template_name = 'custhome/home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
