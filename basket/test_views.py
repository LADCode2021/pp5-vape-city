from django.test import TestCase, Client
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from product.models import Product

# Create your tests here.


class TestViews(TestCase):

    def setUp(self):
        product = Product.objects.create(
            category='disposable_vape',
            slug='test_product',
            sku='0001',
            name='test_product',
            brand='test',
            has_flavours=True,
            has_strength=True,
            description='test description',
            price=decimal('4.99'),
            rating='',
            image_url='',
            image='',
            display_home=True,
            created_at='2023-03-12 14:30:59'
        )

    def test_view_basket(self):
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')
    
    def test_add_to_basket_(self):




