from rest_framework import serializers
from user_directory.models import Users, Location


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    def create(self, validated_data):
        user = Users.objects.create(**validated_data)

        user.set_password(validated_data["password"])
        user.save()

        return user


class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

