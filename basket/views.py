from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    flavour = None
    if 'product_flavour' in request.POST:
        flavour = request.POST['product_flavour']
    basket = request.session.get('basket', {})

    if flavour:
        if item_id in list(basket.keys()):
            if flavour in basket[item_id]['items_by_flavour'].keys():
                basket[item_id]['items_by_flavour'][flavour] += quantity
            else:
                basket[item_id]['items_by_flavour'][flavour] = quantity
        else:
            basket[item_id] = {'items_by_flavour': {flavour: quantity}}
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    flavour = None
    if 'product_flavour' in request.POST:
        flavour = request.POST['product_flavour']
    basket = request.session.get('basket', {})

    if flavour:
        if quantity > 0:
            basket[item_id]['items_by_flavour'][flavour] = quantity
        else:
            del basket[item_id]['items_by_flavour'][flavour]
            if not basket[item_id]['items_by_flavour']:
                basket.pop(item_id)

    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse(view_basket))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        flavour = None
        if 'product_flavour' in request.POST:
            flavour = request.POST['product_flavour']
        basket = request.session.get('basket', {})

        if flavour:
            del basket[item_id]['items_by_flavour'][flavour]
            if not basket[item_id]['items_by_flavour']:
                basket.pop(item_id)
        else:
            basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
