import requests

class ProductConsumer(object):
    def __init__(self, base_uri):
        self.base_uri = base_uri

    def get_product(self, id):
        """Get product by ID"""
        uri = self.base_uri + '/product/' + id
        response = requests.get(uri)
        if response.status_code == 404:
            return None

        json = response.json()
        return Product(json['id'], json['type'], json['name'])


class Product(object):
    def __init__(self, id, type, name ):
        self.id = id
        self.type = type
        self.name = name
