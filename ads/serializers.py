from rest_framework import serializers
from ads.models import Ads


class AdsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = '__all__'