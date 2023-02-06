import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, DetailView, ListView, CreateView, DeleteView
from ads.models import Ads, Categories, Users


def home_page(request):
    return HttpResponse(200, {"status": "ok"})


@method_decorator(csrf_exempt, name="dispatch")
class AdsView(ListView):
    model = Ads
    queryset = Ads.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        ads = []
        for ad in self.object_list:
            ads.append(
                {
                    "id": ad.id,
                    "name": ad.name,
                }
            )
        return JsonResponse(ads, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class AdDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({"статус": ad.status,
                             "название": ad.name,
                             "цена": ad.price,
                             "описание": ad.description,
                             "опубликовано?": ad.is_published})


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ads
    fields = ["name", "price", "description", "is_published", "category", "user_id"]

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        category = get_object_or_404(Categories, ad_data["category"])
        user_id = get_object_or_404(Users, ad_data["user_id"])
        ad, _ = Ads.objects.get_or_create(name=ad_data["name"], price=ad_data["price"], description=ad_data["description"],
                                          is_published=ad_data["is_published"], category=category, user_id=user_id)
        return JsonResponse({
            "name": ad.name,
        }, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateView(UpdateView):
    model = Ads
    fields = ["status", "name", "user_id", "price", "description", "is_published", "image", "category"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES["image"]
        self.object.save()
        return JsonResponse({
            "name": self.object.name,
            "image": self.object.image.url if self.object.image else None
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ads
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"Удаление": "Успешно"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesListView(ListView):
    model = Categories
    queryset = Categories.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        categories = []
        for category in self.object_list:
            categories.append(
                {
                    "id": category.id,
                    "name": category.name,
                }
            )

        return JsonResponse(categories, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({"статус": category.status,
                             "название": category.name,
                             })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Categories
    fields = ["status", "name"]

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)
        category, _ = Categories.objects.get_or_create(name=category_data["name"])
        return JsonResponse({
            "name": category.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Categories
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)
        category = Categories.objects.create(
            name=category_data["name"]
        )
        return JsonResponse({
            "name": category.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Categories
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"Удаление": "Успешно"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class UserView(ListView):
    model = Users
    queryset = Users.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        users = []
        for user in self.object_list:
            users.append(
                {
                    "Имя": user.first_name,
                    "Фамилия": user.last_name,
                    "Логин": user.username
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
        location = get_object_or_404(Users, user_data["location"])
        user, _ = Users.objects.get_or_create(first_name=user_data["first_name"], last_name=user_data["last_name"],
                                              username=user_data["username"],  password=user_data["password"],
                                              age=user_data["age"], location=location)
        return JsonResponse({
            "username": user.username,
        })

