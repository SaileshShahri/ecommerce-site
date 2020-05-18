from django.shortcuts import render
from django.views.generic import DetailView, ListView, View
from .models import Search
from product.models import Product
from django.contrib.auth.decorators import login_required

def productsearchview(request):
    query = request.GET.get('q', None)
    context = { "query" : query }
    if query is not None:
        Search.objects.create(query=query)
        prsearch_list = Product.objects.search(query=query)
        context = {
            'prsearch_list' : prsearch_list,
            }
    return render(request, 'search/product.html', context)
