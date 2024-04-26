from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import (
    ProductSerializer,
    ProductModel,
    ProductUpdateSerializer,
    SaleSerializer,
    SaleCreateSerializer,
    SaleModel,
    SaleDetailModel,
    UserCreateSerializer,
    MyTokenObtainPairSerializer
)
from .models import MyUser
from cloudinary.uploader import upload
from django.db import transaction
from rest_framework_simplejwt.views import TokenObtainPairView
from os import environ
import requests
from datetime import datetime
import mercadopago
from pprint import pprint

class RegisterView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        try:
            email = request.data.get('email')
            user = MyUser.objects.filter(email=email).first()

            if user:
                raise Exception('El usuario ya existe')
        
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            newUser = serializer.save()
            response = self.serializer_class(newUser).data

            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'errors': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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
    serializer_class = SaleCreateSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            # Recuperamos los datos de la solicitud
            data = request.data

            serializer = self.serializer_class(data=data)
            # Validamos los datos
            serializer.is_valid(raise_exception=True)

            user = MyUser.objects.get(id=data['user_id'])

            # Guardamos la venta
            sale = SaleModel.objects.create(
                total=data['total'],
                user_id=user
            )
            sale.save()

            items = []

            # Verificamos si el stock es suficiente
            for item in data['details']:
                productId = item['product_id']
                quantity = item['quantity']

                product = ProductModel.objects.get(id=productId)
                if product.stock < quantity:
                    raise Exception(f'No hay suficiente stock para el producto {product.name}')
                
                product.stock -= quantity
                product.save()

                # Guardamos el detalle de la venta
                saleDetail = SaleDetailModel.objects.create(
                    quantity=quantity,
                    price=item['price'],
                    subtotal=item['subtotal'],
                    product_id=product,
                    sale_id=sale
                )
                saleDetail.save()

                igv = item['price'] * 0.18
                valor_unitario = item['price']
                precio_unitario = item['price'] + igv
                subtotal = item['subtotal']

                items.append({
                    'unidad_de_medida': 'NIU',
                    'codigo': 'P001',
                    'codigo_producto_sunat': '10000000',
                    'descripcion': product.name,
                    'cantidad': quantity,
                    'valor_unitario': valor_unitario,
                    'precio_unitario': precio_unitario,
                    'subtotal': subtotal,
                    'tipo_de_igv': 1,
                    'igv': igv,
                    'total': (item['price'] + igv) * quantity,
                    'anticipo_regularizacion': False
                })

            body = {
                'operacion': 'generar_comprobante',
                'tipo_de_comprobante': 2,
                'serie': 'BBB1',
                'numero': 1,
                'sunat_transaction': 1,
                'cliente_tipo_de_documento': 1,
                'cliente_numero_de_documento': '73201471',
                'cliente_denominacion': 'EMPRESA DE PRUEBA',
                'cliente_direccion': 'AV. LARCO 1234',
                'cliente_email': 'email@email.com',
                'fecha_de_emision': datetime.now().strftime('%d-%m-%Y'),
                'moneda': 1,
                'porcentaje_de_igv': 18.0,
                'total_gravada': 100,
                'total_igv': 18,
                'total': 118,
                'detraccion': False,
                'enviar_automaticamente_a_la_sunat': True,
                'enviar_automaticamente_al_cliente': True,
                'items': items
            }

            nubeFactResponse = requests.post(
                url=environ.get('NUBEFACT_URL'),
                headers={
                    'Authorization': f'Bearer {environ.get("NUBEFACT_TOKEN")}'
                },
                json=body
            )

            json = nubeFactResponse.json()

            if nubeFactResponse.status_code != 200:
                raise Exception(json['errors'])

            return Response({
                'message': 'Venta realizada correctamente'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            transaction.set_rollback(True) # Deshacer la transacción
            return Response({
                'errors': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SaleUpdateView(generics.UpdateAPIView):
    queryset = SaleModel.objects.all()
    serializer_class = SaleSerializer

class SaleDeleteView(generics.DestroyAPIView):
    queryset = SaleModel.objects.all()
    serializer_class = SaleSerializer

class CreateInvoiceView(generics.GenericAPIView):
    serializer_class = SaleSerializer

    def post(self, request):
        try:
            url = environ.get('NUBEFACT_URL')
            token = environ.get('NUBEFACT_TOKEN')

            invoiceData = {
                'operacion': 'generar_comprobante',
                'tipo_de_comprobante': 2,
                'serie': 'BBB1',
                'numero': 1,
                'sunat_transaction': 1,
                'cliente_tipo_de_documento': 1,
                'cliente_numero_de_documento': '73201471',
                'cliente_denominacion': 'EMPRESA DE PRUEBA',
                'cliente_direccion': 'AV. LARCO 1234',
                'cliente_email': 'email@email.com',
                'fecha_de_emision': datetime.now().strftime('%d-%m-%Y'),
                'moneda': 1,
                'porcentaje_de_igv': 18.0,
                'total_gravada': 100,
                'total_igv': 18,
                'total': 118,
                'detraccion': False,
                'enviar_automaticamente_a_la_sunat': True,
                'enviar_automaticamente_al_cliente': True,
                'items': [
                    {
                        'unidad_de_medida': 'NIU',
                        'codigo': 'P001',
                        'codigo_producto_sunat': '10000000',
                        'descripcion': 'ZAPATILLAS PUMBA',
                        'cantidad': 1,
                        'valor_unitario': 100,
                        'precio_unitario': 118,
                        'subtotal': 100,
                        'tipo_de_igv': 1,
                        'igv': 18,
                        'total': 118,
                        'anticipo_regularizacion': False
                    }
                ]
            }

            nubeFactResponse = requests.post(url=url, headers={
                'Authorization': f'Bearer {token}',
            }, json=invoiceData)

            json = nubeFactResponse.json()

            if nubeFactResponse.status_code != 200:
                raise Exception(json['errors'])

            return Response(json, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'errors': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class GetInvoiceView(APIView):
    def get(self, request, tipo_de_comprobante: int, serie: str, numero: int):
        try:
            body = {
                'operacion': 'consultar_comprobante',
                'tipo_de_comprobante': tipo_de_comprobante,
                'serie': serie,
                'numero': numero
            }
            nubeFactResponse = requests.post(
                url=environ.get('NUBEFACT_URL'),
                headers={
                    'Authorization': f'Bearer {environ.get("NUBEFACT_TOKEN")}',
                },
                json=body
            )

            json = nubeFactResponse.json()

            if nubeFactResponse.status_code != 200:
                raise Exception(json['errors'])

            return Response(json, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'errors': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CreatePaymentView(APIView):
    def post(self, request):
        try:
            mp = mercadopago.SDK(environ.get('MP_ACCESS_TOKEN'))

            preference = {
                'items': [
                    {
                        'id': '1234',
                        'title': 'Zapatillas Pumba',
                        'quantity': 1,
                        'currency_id': 'MXN',
                        'unit_price': 200,
                    }
                ],
                'notification_url': 'https://0aaa-181-67-29-232.ngrok-free.app/api/payment/notification'
            }

            mpResponse = mp.preference().create(preference)

            if mpResponse['status'] != 201:
                return Response({
                    'errors': mpResponse['response']['message']
                }, status=status.HTTP_400_BAD_REQUEST)

            return Response(mpResponse['response'], status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'errors': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class NotificationPaymentView(APIView):
    def post(self, request: Request):
        print(request.data)
        print(request.query_params)

        # Crear la confirmación del pago

        return Response({
            'ok': True
        }, status=status.HTTP_200_OK)