from django.contrib import admin
from product.models import Product, Kind


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'mass', 'price', 'description', 'kind', 'image']


@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
