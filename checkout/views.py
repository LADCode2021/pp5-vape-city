from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MfVi9GbWcf4VCYGwaATeqkBAP7hYL3222TFfmUKP2IGJLetEBVOHgfaHUB4lRhAupd5DSvCdAB2ALqipNL7sjcd00gh06P96h',
        'client_secret': 'Test Client Secret',
    }

    return render(request, template, context)