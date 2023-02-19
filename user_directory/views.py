from django.db.models import Count
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from user_directory.models import Users, Location
from user_directory.serializers import UserSerializers, LocationSerializers


class UsersView(ListAPIView):
    queryset = Users.objects.annotate(ad=Count("ads"))
    serializer_class = UserSerializers


class UserDetailView(RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers


class UserCreateView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers


class UserUpdateView(UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers


class UserDeleteView(DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers


class LocationsViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializers
