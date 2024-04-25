from rest_framework import serializers
from .models import (
    ProductModel,
    SaleModel,
    SaleDetailModel,
    MyUser
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = '__all__'

    def save(self):
        try:
            name = self.validated_data['name']
            document_type = self.validated_data['document_type']
            document_number = self.validated_data['document_number']
            email = self.validated_data['email']
            password = self.validated_data['password']

            user = MyUser(
                document_type=document_type,
                document_number=document_number,
                email=email,
                name=name,
            )
            user.set_password(password)
            user.save()
            return user
        except KeyError as e:
            print(e, 1000000000000)
            raise serializers.ValidationError(f'Error: {e}')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

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
