from rest_framework import serializers
from .models import (
    ProductModel,
    SaleModel,
    SaleDetailModel
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
        # fields = ['id', 'name']
        # exclude = ['id', 'name']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = instance.image.url
        return representation

class ProductUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)
    price = serializers.FloatField(required=False)
    stock = serializers.IntegerField(required=False)
    status = serializers.BooleanField(required=False)

    class Meta:
        model = ProductModel
        fields = '__all__'

# Serializador para listar ventas
class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetailModel
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    details = SaleDetailSerializer(source='saleDetails', many=True)
    class Meta:
        model = SaleModel
        fields = '__all__'

# Serializador para crear venta
class SaleDetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetailModel
        exclude = ['sale_id']

class SaleCreateSerializer(serializers.ModelSerializer):
    details = SaleDetailCreateSerializer(source='saleDetails', many=True)

    class Meta:
        model = SaleModel
        fields = '__all__'