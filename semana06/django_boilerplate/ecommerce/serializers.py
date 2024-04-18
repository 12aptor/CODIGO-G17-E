from rest_framework import serializers
from .models import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
        # fields = ['id', 'name']
        # exclude = ['id', 'name']