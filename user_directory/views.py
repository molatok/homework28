import json
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, UpdateView, DeleteView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from user_directory.models import Users, Location
from user_directory.serializers import UserSerializers, LocationSerializers


class UsersView(ListAPIView):
    queryset = Users.objects.annotate(ad=Count("ads"))
    serializer_class = UserSerializers


@method_decorator(csrf_exempt, name="dispatch")
class UserDetailView(DetailView):
    model = Users

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return JsonResponse({"Имя": user.first_name,
                             "Фамилия": user.last_name,
                             "Логин": user.username})


class UserCreateView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = Users
    fields = ["first_name", "last_name", "username", "password", "age", "location"]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        user = Users.objects.create(
            first_name=user_data["first_name"], last_name=user_data["last_name"],
            username=user_data["username"], password=user_data["password"],
            age=user_data["age"]
        )

        return JsonResponse({
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = Users
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"Удаление": "Успешно"}, status=200)


class LocationsViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializers
