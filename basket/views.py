from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    flavour = None
    strength = None

    if 'product_flavour' and 'product_strength' in request.POST:
        flavour_id = request.POST['product_flavour_id']
        strength_id = request.POST['product_strength_id']
        item = f'{item_id}_{flavour_id}_{strength_id}'
        print(item)

    if 'product_flavour' in request.POST:
        flavour = request.POST['product_flavour']
    if 'product_strength' in request.POST:
        strength = request.POST['product_strength']
    basket = request.session.get('basket', {})

    if flavour:
        if item_id in list(basket.keys()):
            if flavour in basket[item_id]['items_by_flavour'].keys():
                basket[item_id]['items_by_flavour'][flavour] += quantity
                messages.success(request, f'Updated {product.name} flavour {flavour.upper()} quantity to {basket[item_id]["items_by_flavour"][flavour]}')
            else:
                basket[item_id]['items_by_flavour'][flavour] = quantity
                messages.success(request, f'Added {product.name} flavour {flavour.upper()} to your basket')
        else:
            basket[item_id] = {'items_by_flavour': {flavour: quantity}}
            messages.success(request, f'Added {product.name} flavour {flavour.upper()} to your basket')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {basket[item_id]}')
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    print(basket)
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust the quantity of the specified product to the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    flavour = None
    if 'product_flavour' in request.POST:
        flavour = request.POST['product_flavour']
    basket = request.session.get('basket', {})

    if flavour:
        if quantity > 0:
            basket[item_id]['items_by_flavour'][flavour] = quantity
            messages.success(request, f'Updated {product.name} flavour {flavour.upper()} quantity to {basket[item_id]["items_by_flavour"][flavour]}')
        else:
            del basket[item_id]['items_by_flavour'][flavour]
            if not basket[item_id]['items_by_flavour']:
                basket.pop(item_id)
            messages.success(request, f'Removed {product.name} flavour {flavour.upper()} from your basket')

    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {basket[item_id]}')
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse(view_basket))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        flavour = None
        if 'product_flavour' in request.POST:
            flavour = request.POST['product_flavour']
        basket = request.session.get('basket', {})

        if flavour:
            del basket[item_id]['items_by_flavour'][flavour]
            if not basket[item_id]['items_by_flavour']:
                basket.pop(item_id)
            messages.success(request, (f'Removed 'f'{product.name} flavour {flavour.upper()} from your basket'))
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
