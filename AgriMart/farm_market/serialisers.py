from rest_framework import serializers
from .models import Farmer, Product, Cart, CartItem, Order, DeliveryCrew

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    farmer = FarmerSerializer()  # Nested serializer for farmer detail

    class Meta:
        model = Product
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Nested serializer for product detail

    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(many=True, required=False)  # Nested serializer for cart items

    class Meta:
        model = Cart
        fields = '__all__'

class DeliveryCrewSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = DeliveryCrew
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer()  # Nested serializer for cart detail

    class Meta:
        model = Order
        fields = '__all__'