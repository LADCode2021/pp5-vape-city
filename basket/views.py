from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
    )
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

    item = None
    if 'product_flavour' and 'product_strength' in request.POST:
        flavour = request.POST['product_flavour']
        strength = request.POST['product_strength']
        item = f'{item_id}_{flavour}_{strength}'
    basket = request.session.get('basket', {})

    if item:
        if item_id in list(basket.keys()):
            if item in basket[item_id]['items_by_variation'].keys():
                basket[item_id]['items_by_variation'][item] += quantity
                messages.success(
                    request, f'Updated {product.name}'
                    f'flavour {flavour.upper()} quantity to'
                    f'{basket[item_id]["items_by_variation"][item]}'
                    )
            else:
                basket[item_id]['items_by_variation'][item] = quantity
                messages.success(
                    request,
                    f'Added {product.name}'
                    f'flavour {flavour.upper()} to your basket'
                    )
        else:
            basket[item_id] = {'items_by_variation': {item: quantity}}
            messages.success(
                request,
                f'Added {product.name}'
                f'flavour {flavour.upper()} to your basket'
                )
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {basket[item_id]}'
                )
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
    item = None
    if 'product_item' in request.POST:
        flavour = request.POST['product_flavour']
        strength = request.POST['product_strength']
        item = f'{item_id}_{flavour}_{strength}'
    basket = request.session.get('basket', {})

    if item:
        if quantity > 0:
            basket[item_id]['items_by_variation'][item] = quantity
            messages.success(
                request, f'Updated {product.name}'
                f'flavour {flavour.upper()} quantity to'
                f'{basket[item_id]["items_by_variation"][item]}'
                )
        else:
            del basket[item_id]['items_by_variation'][item]
            if not basket[item_id]['items_by_variation']:
                basket.pop(item_id)
            messages.success(
                request,
                f'Removed {product.name}'
                f'flavour {flavour.upper()} from your basket'
                )
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {basket[item_id]}'
                )
        else:
            basket.pop(item_id)
            messages.success(
                request,
                f'Removed {product.name} from your basket'
                )

    request.session['basket'] = basket
    return redirect(reverse(view_basket))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        item = None
        if 'product_item' in request.POST:
            item = request.POST['product_item']
            flavour = item.split('_')[1]
            strength = item.split('_')[2]
        basket = request.session.get('basket', {})

        if item:
            del basket[item_id]['items_by_variation'][item]
            if not basket[item_id]['items_by_variation']:
                basket.pop(item_id)
            messages.success(
                request,
                f'Removed 'f'{product.name}'
                f'Flavour - {flavour.upper()}'
                f'Strength - {strength.upper()} from your basket'
                )
        else:
            basket.pop(item_id)
            messages.success(
                request,
                f'Removed {product.name} from your basket'
                )

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        print(e)
        return HttpResponse(status=500)
