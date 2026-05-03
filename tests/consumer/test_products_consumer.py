"""pact test for product service client"""

import logging
from typing import Generator

import pytest
from pact import Pact, match

from src.consumer import ProductConsumer

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope='session')
def pact() -> Generator[Pact, None, None]:
    pact = Pact('pactflow-example-consumer-python', 'pactflow-example-provider-python')
    yield pact.with_specification('V4')
    pact.write_file('./pacts')


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
     .with_body(match.like(expected)))

    with pact.serve() as srv:
        consumer = ProductConsumer(str(srv.url))
        user = consumer.get_product('10')
        assert user.name == 'Margharita'
