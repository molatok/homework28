import pytest

from ads.models import Ads


@pytest.mark.django_db
def test_ads_list(client):
    ad = Ads.objects.create(
        {
            "name": "Now this field is required.",
            "price": 1,
            "description": "This field is required.",
            "is_published": "False",
            "user": 3
        }
    )

    expected_response = {
        {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": ad.pk,
                    "status": "draft",
                    "name": "ow this field is required.",
                    "price": 1,
                    "description": "This field is required.",
                    "is_published": "False",
                    "user": 3,
                }
            ]
        }
    }

    response = client.get("/ads/")

    assert response.status_code == 200
    assert response.data == expected_response
