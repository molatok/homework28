from rest_framework import serializers
from user_directory.models import Users, Location


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

