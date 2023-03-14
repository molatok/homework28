import pytest
from ads.models import Ads


@pytest.mark.django_db
def test_ads_list(client):

    # тест на выдачу списка

    ad = Ads.objects.create(
        name="Test name 12345678",
        price=1,
        description="Test 22 description",
        is_published="draft",
    )

    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{
            "id": ad.pk,
            "status": "draft",
            "name": "Test name 12345678",
            "price": 1,
            "description": "Test 22 description",
            "is_published": "draft",
            "image": None,
            "user": None,
            "category": None
        }]
    }

    response = client.get("/ads/")

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_get_one_ad(client, test_token):

    # тест на создание и выдачу одного объявления

    ad = Ads.objects.create(
        name="Test name 12345678",
        price=1,
        description="Test 22 description",
        is_published="draft",
    )

    expected_response = {
            "id": ad.pk,
            "status": "draft",
            "name": "Test name 12345678",
            "price": 1,
            "description": "Test 22 description",
            "is_published": "draft",
            "image": None,
            "user": None,
            "category": None
        }

    response = client.get(f"/ads/{ad.pk}/",
                          HTTP_AUTHORIZATION="Token " + test_token)

    assert response.status_code == 200
    assert response.data == expected_response
