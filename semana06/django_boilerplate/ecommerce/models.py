from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')
    price = models.FloatField()
    stock = models.IntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

class SaleModel(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.FloatField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sales'

    def __str__(self) -> str:
        return self.id

class SaleDetailModel(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    subtotal = models.FloatField()
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    sale_id = models.ForeignKey(SaleModel, on_delete=models.CASCADE, related_name='saleDetails')

    class Meta:
        db_table = 'sale_details'

    def __str__(self) -> str:
        return self.id