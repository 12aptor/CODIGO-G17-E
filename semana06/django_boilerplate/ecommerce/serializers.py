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

class SaleDetailSerializer(serializers.ModelSerializer):
    sale_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = SaleDetailModel
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    details = SaleDetailSerializer(many=True)
    class Meta:
        model = SaleModel
        fields = '__all__'