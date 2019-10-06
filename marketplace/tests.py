import json
from rest_framework.test import APIClient
from django.test import TestCase
from marketplace.models import Client
from marketplace.mock_data import product_helper, client_helper
from django.contrib.auth.models import User


def _ld_rsp(response):
    return json.loads(response.content.decode())


class APITestCase(TestCase):

    def _test_creating_clients(self, client, c1, c2, c3):

        client.post('/api/clients/', c1)

        client1 = Client.objects.get(name='Client1')
        self.assertEqual(client1.email, 'client1@email.com')

        self.assertEqual(_ld_rsp(client.get('/api/clients/')).get('count'), 1)

        client.post('/api/clients/', c2)

        client.post('/api/clients/', c3)

        self.assertEqual(_ld_rsp(client.get('/api/clients/')).get('count'), 3)

    def _test_repeated_client_email(self, client, c4):
        rpt_rsp = client.post('/api/clients/', c4)

        self.assertEqual(rpt_rsp.status_code, 400)

        self.assertEqual(_ld_rsp(rpt_rsp)['email'][0],
                         'client with this email already exists.')

    def _test_update_client(self, client, c6):
        self.assertEqual(client.put('/api/clients/3', c6).status_code, 200)
        self.assertTrue(Client.objects.get(email='client3new@email.com'))

    def _test_setting_list_of_favorites(self, client, c5):
        self.assertEqual(client.put('/api/clients/3', c5).status_code, 200)
        self.assertTrue(Client.objects.get(productslist=c5['productslist']))

    def _test_creating_products(self, client, p1, p2, p3):
        client.post('/api/product/', p1, format='json')
        client.post('/api/product/', p2, format='json')
        client.post('/api/product/', p3, format='json')

        self.assertEqual(_ld_rsp(client.get('/api/product/')).get('count'), 3)

    def cases(self):
        client = APIClient()
        user = User.objects.create(username='admin')
        client.force_login(user=user)

        c1, c2, c3, c4, c5, c6 = client_helper()
        p1, p2, p3 = product_helper()

        self._test_creating_clients(client, c1, c2, c3)
        self._test_repeated_client_email(client, c4)
        self._test_creating_products(client, p1, p2, p3)
        self._test_update_client(client, c6)
        self._test_setting_list_of_favorites(client, c5)