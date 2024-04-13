from django.contrib import admin
from .models import ProductsModel

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'description')
    list_per_page = 10

admin.site.register(ProductsModel, ProductsAdmin)