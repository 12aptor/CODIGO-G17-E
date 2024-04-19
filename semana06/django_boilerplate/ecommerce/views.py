from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import (
    ProductSerializer,
    ProductModel,
    ProductUpdateSerializer,
    SaleSerializer,
    SaleModel
)
from cloudinary.uploader import upload


class ProductView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(generics.UpdateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductUpdateSerializer

class ProductDeleteView(generics.DestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.status = False
            instance.save()

            return Response({
                'message': 'Producto eliminado correctamente'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'errors': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProductUploadImageView(generics.GenericAPIView):
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        try:
            # Obtenemos el archivo de imagen
            imageFile = request.FILES.get('image')

            if not imageFile:
                raise Exception('No se ha enviado ninguna imagen')

            # Subir la imagen a cloudinary
            uploadedImage = upload(imageFile)
            imageName = uploadedImage['secure_url'].split('/')[-1]
            imagePath = f'{uploadedImage["resource_type"]}/{uploadedImage["type"]}/v{uploadedImage["version"]}/{imageName}'

            # Retornar la URL de la imagen subida
            return Response({
                'url': imagePath
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'errors': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SaleView(generics.ListAPIView):
    queryset = SaleModel.objects.all()
    serializer_class = SaleSerializer

class SaleCreateView(generics.CreateAPIView):
    queryset = SaleModel.objects.all()
    serializer_class = SaleSerializer

    def create(self, request, *args, **kwargs):
        try:
            # Recuperamos los datos de la solicitud
            data = request.data

            # Verificamos si el stock es suficiente
            for item in data['detail']:
                productId = item['product_id']
                quantity = item['quantity']

                product = ProductModel.objects.get(id=productId)
                if product.stock < quantity:
                    raise Exception(f'No hay suficiente stock para el producto {product.name}')

            return Response({
                'ok': True
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'errors': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SaleUpdateView(generics.UpdateAPIView):
    queryset = SaleModel.objects.all()
    serializer_class = SaleSerializer

class SaleDeleteView(generics.DestroyAPIView):
    queryset = SaleModel.objects.all()
    serializer_class = SaleSerializer