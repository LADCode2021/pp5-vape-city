from django.contrib import admin
from .models import Product, Category, Flavour, Strength


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'brand',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Flavour)
admin.site.register(Strength)
