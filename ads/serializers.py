from rest_framework import serializers
from ads.models import Ads, Collection


class AdsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = '__all__'


class CollectionSerializers(serializers.ModelSerializer):
    items = AdsSerializers(many=True)

    class Meta:
        model = Collection
        fields = '__all__'


class CollectionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name']


class CollectionUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name']


class CollectionCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
