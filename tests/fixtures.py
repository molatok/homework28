import pytest


@pytest.fixture
@pytest.mark.django_db
def test_token(client, django_user_model):
    username = "admin"
    user = django_user_model.objects.create(
        username=username
    )
    user.set_password('pbkdf2_sha256$260000$BmB5PD7JptwhCgCDTtzW2f$g0kLK32zzwhk7tuW5ZIw0WQ45ZRLm7sOL1pMlbj0uPQ=')
    user.save()
    response = client.post(
        "/login/",
        {"username": username, "password": "pbkdf2_sha256$260000$BmB5PD7JptwhCgCDTtzW2f$g0kLK32zzwhk7tuW5ZIw0WQ45ZRLm7sOL1pMlbj0uPQ="},
        format="json"
    )
    return response.data['token']