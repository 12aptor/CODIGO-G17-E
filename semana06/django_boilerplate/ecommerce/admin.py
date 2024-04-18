from django.contrib import admin
from .models import (
    ProductModel,
    SaleModel,
    SaleDetailModel,
)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'status', 'created_at', 'updated_at')

admin.site.register(ProductModel, ProductAdmin)
admin.site.register(SaleModel)
admin.site.register(SaleDetailModel)