from marketplace.models import Product, Client
from marketplace.serializers import ClientSerializer, ProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ClientView(ListCreateAPIView):
    queryset = Client.objects.get_queryset().order_by('id')
    serializer_class = ClientSerializer


class SingleClientView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.get_queryset().order_by('id')
    serializer_class = ClientSerializer


class ProductView(ListCreateAPIView):
    queryset = Product.objects.get_queryset().order_by('id')
    serializer_class = ProductSerializer


class SingleProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.get_queryset().order_by('id')
    serializer_class = ProductSerializer
