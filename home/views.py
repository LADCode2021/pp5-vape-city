from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page and products"""
    products = Product.objects.filter(display_home=True)
    context = {
        'products': products
    }
    return render(request, "home/index.html", context)


def delivery_information(request):
    """ A view to return the index page and products"""
    return render(request, "home/delivery_information.html")


def privacy_policy(request):
    """ A view to return the index page and products"""
    return render(request, "home/privacy_policy.html")
