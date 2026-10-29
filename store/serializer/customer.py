import re

from rest_framework import serializers
from store.models import Customer
from store.serializer import AddressSerializer


class CustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['date_joined']

class CustomerCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address']

    def validate_phone_number(self, value):
        if re.match(r'^\+?1?\d{9,15}$', value):
            raise serializers.ValidationError('Номер должен состоять из 10-15 цифр')
        return value



