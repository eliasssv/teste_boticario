from rest_framework import serializers
from .models import Seller, Order

class SellerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer of Seller
    \n@since 2020-08-22
    \n@author eliasssv
    """
    class Meta:
        model = Seller
        fields = ['id', 'fullname', 'cpf', 'email', 'created_at', 'updated_at']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer of Order
    \n@since 2020-08-22
    \n@author eliasssv
    """
    class Meta:
        model = Order
        fields = ['code', 'value', 'status', 'date', 'seller', 'created_at', 'updated_at']   