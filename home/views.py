from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page and products"""
    products = Product.objects.filter(display_home=True)
    context = {
        'products': products
    }
    return render(request, "home/index.html", context)
