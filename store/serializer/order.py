from rest_framework import serializers
from store.models import Order
from store.serializer import CustomerSerializer


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('order_date',)


class OrderCrateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('order_date',)