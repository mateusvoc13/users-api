import logging
from marketplace.models import Product, Client, idGenerator
from marketplace.serializers import ClientSerializer, ProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


logger = logging.getLogger('exceptions')
_default_image_url = 'http://challenge-api.luizalabs.com/images/%s'


class ClientView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Client.objects.get_queryset().order_by('id')
    serializer_class = ClientSerializer


class SingleClientView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Client.objects.get_queryset().order_by('id')
    serializer_class = ClientSerializer


class ProductView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.get_queryset().order_by('id')
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):

        try:
            request.data._mutable = True
        except Exception:
            logger.error('Mutable is not available')
            pass

        if not request.data.get('id'):
            request.data.update({'id': idGenerator(request.data)})

        if not request.data.get('image'):
            _image_url = _default_image_url % (request.data.get(id) or idGenerator(request.data))
            request.data.update({'image': _image_url})

        return super(ProductView, self).create(request, *args, **kwargs)


class SingleProductView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.get_queryset().order_by('id')
    serializer_class = ProductSerializer
