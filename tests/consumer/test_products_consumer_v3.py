"""pact test for product service client via rust core"""

import logging
from typing import Generator

import pytest
from pact.v3.pact import Pact
from pact.v3.match import like
from src.consumer import ProductConsumer

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@pytest.fixture(scope='session')
def pact() -> Generator[Pact, None, None]:
    pact = Pact("pactflow-example-consumer-python-v3", "pactflow-example-provider-python-v3")
    yield pact.with_specification("V4")
    pact.write_file("./pacts")

def test_get_product(pact) -> None:
    expected = {
        'id': "27",
        'name': 'Margharita',
        'type': 'Pizza'
    }

    (pact
     .upon_receiving('a request to get a product')
     .given('a product with ID 10 exists')
     .with_request(method='GET', path='/product/10')
     .will_respond_with(200)
     .with_body(like(expected)))

    with pact.serve() as srv:
        consumer = ProductConsumer(str(srv.url))
        user = consumer.get_product('10')
        assert user.name == 'Margharita'
