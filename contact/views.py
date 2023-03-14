from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def make_contact(request):
    """
    Get contact page and post ContactForm to db.
    """

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Successfully made contact')
            return redirect(reverse('make_contact'))
        else:
            messages.error(
                request,
                'Failed to make contact. Please ensure the form is valid.'
                )
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
