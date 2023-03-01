import json
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, DetailView, ListView, CreateView, DeleteView
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from ads.models import Ads, Categories, Collection
from ads.serializers import AdsSerializers, CollectionSerializers, CollectionCreateSerializers, \
    CollectionListSerializers, CollectionUpdateSerializers
from user_directory.permissions import IsOwnerOrAdmin, IsOwner


def home_page(request):
    return HttpResponse(200, {"status": "ok"})


class AdsListView(ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializers

    def get(self, request, *args, **kwargs):
        category = request.GET.getlist('cat', [])
        if category:
            self.queryset = self.queryset.filter(category_id__in=category)

        text = request.GET.get('text')
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get('location')
        if location:
            self.queryset = self.queryset.filter(user_id__location__name__icontains=location)

        price_from = request.GET.get('price_from')
        price_to = request.GET.get('price_to')
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().get(self, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ads.objects.annotate()
    serializer_class = AdsSerializers
    permission_classes = [IsAuthenticated]


class AdCreateView(CreateAPIView):
    queryset = Ads.objects.annotate()
    serializer_class = AdsSerializers
    permission_classes = [IsAuthenticated]


class AdUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    queryset = Ads.objects.all()
    serializer_class = AdsSerializers


class AdDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    queryset = Ads.objects.all()
    serializer_class = AdsSerializers


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesListView(ListView):
    model = Categories
    queryset = Categories.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by("name")

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


class CollectionView(ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionListSerializers


class CollectionDetailView(RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializers


class CollectionCreateView(CreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionCreateSerializers


class CollectionUpdateView(UpdateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionUpdateSerializers
    permission_classes = [IsAuthenticated, IsOwner]


class CollectionDeleteView(DestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializers
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]