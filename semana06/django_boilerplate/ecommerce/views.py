from rest_framework import generics
from rest_framework.response import Response
from .serializers import (
    ProductSerializer,
    ProductModel,
    ProductUpdateSerializer
)
from cloudinary.uploader import upload


class ProductView(generics.ListCreateAPIView):
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

class ProductUploadImageView(generics.GenericAPIView):
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
            })
        except Exception as e:
            return Response({
                'errors': str(e)
            }, status=500)