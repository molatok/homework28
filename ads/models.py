from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from user_directory.models import Users
from .validators import *


class Categories(models.Model):
    STATUS = [
        ('draft', 'Черновик категории'),
        ('published', 'Размещенная категория'),
        ('closed', 'Закрытая категория')
    ]

    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    name = models.CharField(max_length=20)
    slug = models.CharField(validators=[MinLengthValidator(10)], max_length=50, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ads(models.Model):
    STATUS = [
        ('draft', 'Черновик объявления'),
        ('published', 'Опубликованное объявление'),
        ('closed', 'Снято с публикации')
    ]

    status = models.CharField(max_length=50, choices=STATUS, default='draft')
    name = models.CharField(max_length=50, validators=[MinLengthValidator(10)], null=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(null=False)
    is_published = models.CharField(max_length=5, validators=[check_published_status])
    image = models.ImageField(upload_to="images/", null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Collection(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="collections", null=True)
    name = models.CharField(max_length=300, unique=True)
    items = models.ManyToManyField(Ads)

    class Meta:
        verbose_name = "Пользовательская подборка"
        verbose_name_plural = "Пользовательские подборки"

    def __str__(self):
        return self.name
