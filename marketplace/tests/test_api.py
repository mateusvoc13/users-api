import json
from rest_framework.test import APIClient
from django.test import TestCase
from marketplace.models import Client
from marketplace.mock_data import product_helper, client_helper, mock_admin
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


def _ld_rsp(response):
    return json.loads(response.content.decode())


def create_admin_and_token():
    user = User.objects.create_superuser(username='admin',
                                         email='email1@email.com',
                                         password='adminadmin')
    user.save()
    Token.objects.create(user=user)
    return user


class APITestCase(TestCase):

    def _test_creating_clients(self, client, c1, c2, c3):
        """
        Aims to verify if the create and view methods of the Clients API
        are working as expected and if the changes are being reflected
        in the database.

        """
        client.post('/api/clients/', c1)

        client1 = Client.objects.get(name='Client1')
        self.assertEqual(client1.email, 'client1@email.com')
        self.assertEqual(_ld_rsp(client.get('/api/clients/')).get('count'), 1)

        client.post('/api/clients/', c2)
        client.post('/api/clients/', c3)
        self.assertEqual(_ld_rsp(client.get('/api/clients/')).get('count'), 3)

    def _test_repeated_client_email(self, client, c4):
        """
        Aims to verify if the 'unique' constraint of the email field is
        being respected by the API.

        """
        rpt_rsp = client.post('/api/clients/', c4)

        self.assertEqual(rpt_rsp.status_code, 400)

        self.assertEqual(_ld_rsp(rpt_rsp)['email'][0],
                         'client with this email already exists.')

    def _test_update_client(self, client, c6):
        self.assertEqual(client.put('/api/clients/3', c6).status_code, 200)
        self.assertTrue(Client.objects.get(email='client3new@email.com'))

    def _test_remove_client(self, client, c6):
        """
        Aims to verify if the delete method works as expected in the
        Clients API and ifthe number of clients in the database drops
        after the procedure.

        """
        self.assertEqual(Client.objects.all().count(), 3)
        self.assertEqual(client.delete('/api/clients/3').status_code, 204)
        self.assertEqual(Client.objects.all().count(), 2)

    def _test_setting_list_of_favorites(self, client, c5):
        """
        Aims to verify if the API allows setting the list of favorites
        through a PUT method and if the update is reflected in the
        database.

        """
        self.assertEqual(client.put('/api/clients/3', c5).status_code, 200)
        self.assertTrue(Client.objects.get(productslist=c5['productslist']))

    def _test_creating_products(self, client, p1, p2, p3):
        """
        Aims to verify if the API allows to create products using the
        format that comes from the mock_data file and

        """
        client.post('/api/product/', p1, format='json')
        client.post('/api/product/', p2, format='json')
        client.post('/api/product/', p3, format='json')

        self.assertEqual(_ld_rsp(client.get('/api/product/')).get('count'), 3)

    def test_cases(self):
        """
        Aims to organize the test cases in a single place managing
        execution order and if all the expected scenarios are present.

        """
        client = APIClient()
        user = create_admin_and_token()
        token_request = client.post('/api-token-auth/', mock_admin(),  format='json')
        self.assertEqual(token_request.status_code, 200)
        token2 = json.loads(token_request.content.decode()).get('token')

        client.credentials(HTTP_AUTHORIZATION='Token ' + token2)
        client.force_login(user=user)

        c1, c2, c3, c4, c5, c6 = client_helper()
        p1, p2, p3 = product_helper()

        self._test_creating_clients(client, c1, c2, c3)
        self._test_repeated_client_email(client, c4)
        self._test_creating_products(client, p1, p2, p3)
        self._test_update_client(client, c6)
        self._test_setting_list_of_favorites(client, c5)
        self._test_remove_client(client, c3)
