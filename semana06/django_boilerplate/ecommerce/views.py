from rest_framework import generics
from .serializers import ProductSerializer, ProductModel


class ProductView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer