import factory.django
from ads.models import Ads, Collection
from user_directory.models import Users


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Users

    username = "admin3"
    password = "12345678"
    email = "admin2@admin2.ru"


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ads

    name = "Test name 12345678",
    price = 1,
    description = "Test 22 description",
    is_published = "draft"
    user = factory.SubFactory(UserFactory)


class CollectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Collection

    name = factory.Faker("word"),
    items: [1, 2, 4]



