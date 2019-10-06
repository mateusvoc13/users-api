from rest_framework import serializers
from marketplace.models import Client, Product


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'email', 'productslist')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'image', 'brand', 'reviewScore')
