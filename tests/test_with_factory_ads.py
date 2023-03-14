import pytest

from ads.serializers import CollectionListSerializers
from tests.factories import CollectionFactory


@pytest.mark.django_db
def test_create_collection(client, collection):
    # тест на создание подборки с использованием фабрики

    collection = CollectionFactory.create_batch(1)
    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": CollectionListSerializers(collection, many=True).data

    }

    response = client.get("/collections/")

    assert response.status_code == 200
    assert response.data == expected_response
