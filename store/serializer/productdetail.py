from rest_framework import serializers
from store.models import ProductDetail
from store.serializer import ProductSerializer


class ProductDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductDetail
        fields = '__all__'


class ProductDetailCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'