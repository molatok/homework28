import json
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from user_directory.models import Users, Location


@method_decorator(csrf_exempt, name="dispatch")
class UsersView(ListView):
    model = Users
    queryset = Users.objects.annotate(ad=Count("ads"))

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by("username")
        users = []
        for user in self.object_list:
            users.append(
                {
                    "Имя": user.first_name,
                    "Фамилия": user.last_name,
                    "Логин": user.username,
                    "opa": user.ad
                }
            )
        return JsonResponse(users, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class UserDetailView(DetailView):
    model = Users

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return JsonResponse({"Имя": user.first_name,
                             "Фамилия": user.last_name,
                             "Логин": user.username})


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = Users
    fields = ["first_name", "last_name", "username", "password", "age", "location"]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        user, _ = Users.objects.get_or_create(first_name=user_data["first_name"], last_name=user_data["last_name"],
                                              username=user_data["username"], password=user_data["password"],
                                              age=user_data["age"])
        location, _ = Location.objects.get_or_create(name=user_data["location"])
        user.location.add(location)

        return JsonResponse({
            "username": user.username,
        })


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
