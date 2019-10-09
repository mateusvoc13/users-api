from marketplace.models import idGenerator


def mock_product1():
    return {
        'title': 'Product1',
        'price': '300.10',
        'brand': 'Brand1',
        'reviewscore': '13'
    }


def mock_product2():
    return {
        'title': 'Product2',
        'price': '5.15',
        'image': 'http://google.com',
        'brand': 'Brand2',
        'reviewscore': '5'
    }


def mock_admin():
    return {
        'username': 'admin',
        'password': 'adminadmin',
    }


def mock_product3():
    return {
        'title': 'Product3',
        'price': '41.33',
        'image': 'http://google.com',
        'brand': 'Brand3',
        'reviewscore': '1',
    }


def mock_client1():
    return {
        'name': 'Client1',
        'email': 'client1@email.com'
    }


def mock_client2():
    return {
        'name': 'Client2',
        'email': 'client2@email.com'
    }


def mock_client3():
    return {
        'name': 'Client3',
        'email': 'client3@email.com'
    }


def mock_client_repeated_email():
    return {
        'name': 'RepeatedClient',
        'email': 'client1@email.com'
    }


def mock_client_with_product_list():
    return {
        'name': 'Client3',
        'email': 'client3@email.com',
        'productslist': idGenerator(mock_product1())
    }


def mock_client_update():
    return {
        'name': 'Client3',
        'email': 'client3new@email.com'
    }


def product_helper():
    return mock_product1(), mock_product2(), mock_product3()


def client_helper():
    return (mock_client1(),
            mock_client2(),
            mock_client3(),
            mock_client_repeated_email(),
            mock_client_with_product_list(),
            mock_client_update())
