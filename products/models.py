from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    ordering = ('name',)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Variation(models.Model):
    product = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.SET_NULL
        )
    flavour = models.CharField(max_length=254, null=True, blank=True)
    strength = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.product) + " | " + self.flavour + " | " + self.strength


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    slug = models.SlugField()
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    brand = models.TextField()
    has_flavours = models.BooleanField(default=False, null=True, blank=True)
    has_strength = models.BooleanField(default=False, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    display_home = models.BooleanField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
