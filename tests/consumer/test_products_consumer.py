"""pact test for product service client via ruby core"""

import logging
import os

import pytest
from pact import Consumer, Like, Provider, Term, Format

from src.consumer import ProductConsumer

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
print(Format().__dict__)

PACT_MOCK_HOST = 'localhost'
PACT_MOCK_PORT = 1234
PACT_DIR = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def consumer():
    return ProductConsumer(
        'http://{host}:{port}'
        .format(host=PACT_MOCK_HOST, port=PACT_MOCK_PORT)
    )


@pytest.fixture(scope='session')
def pact(request):
    pact = Consumer('pactflow-example-consumer-python').has_pact_with(
        Provider('pactflow-example-provider-python'), host_name=PACT_MOCK_HOST, port=PACT_MOCK_PORT,
        pact_dir="./pacts", log_dir="./logs")
    try:
        print('start service')
        pact.start_service()
        yield pact
    finally:
        print('stop service')
        pact.stop_service()

def test_get_product(pact, consumer):
    expected = {
        'id': "27",
        'name': 'Margharita',
        'type': 'Pizza'
    }

    (pact
     .given('a product with ID 10 exists')
     .upon_receiving('a request to get a product')
     .with_request('GET', '/product/10')
     .will_respond_with(200, body=Like(expected)))

    with pact:
        user = consumer.get_product('10')
        assert user.name == 'Margharita'
