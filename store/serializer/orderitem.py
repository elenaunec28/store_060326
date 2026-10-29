from rest_framework import serializers
from store.models import OrderItem
from store.serializer import ProductSerializer, OrderSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemCrateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

        def validate_quantity(self, value):
            if value > 1000:
                raise serializers.ValidationError("Quantity can't be more than 1000.")
            return value

        