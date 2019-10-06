import requests
import json
from django.core.management.base import BaseCommand
from marketplace.models import Product


def _make_json_request(page=1, method='get'):
    headers = {'Content-Type': 'application/json'}
    url = 'http://challenge-api.luizalabs.com/api/product/?page=%s' % (page)
    request = requests.request(method, url, headers=headers)
    return request


class Command(BaseCommand):

    def handle(self, *args, **options):
        page = 1
        request = _make_json_request(page)
        while request.status_code != 404:
            request = _make_json_request(page)
            if request.status_code == 200:
                request_json = json.loads(request.content.decode())['products']

                for product in request_json:
                    try:
                        Product.objects.create(**product)
                    except Exception as e:
                        print(e)
                page = page + 1
