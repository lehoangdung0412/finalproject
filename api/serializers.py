from rest_framework import serializers
from . import models


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model: models.Customer
        fields = '__all__'


# class SupplierSerializer(serializers.ModelSerializer):
#     class Meta:
#         model: models.Supplier
#         fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model: models.Payment
        fields = '__all__'


class ShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model: models.Shipper
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model: models.Delivery
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model: models.OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model: models.Order
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model: models.Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model: models.Category
        fields = '__all__'
