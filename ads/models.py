from django.db import models
from user_directory.models import Users


class Categories(models.Model):
    STATUS = [
        ('draft', 'Черновик категории'),
        ('published', 'Размещенная категория'),
        ('closed', 'Закрытая категория')
    ]

    status = models.CharField(max_length=30, choices=STATUS, default='draft')
    name = models.CharField(max_length=50)

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
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    is_published = models.CharField(max_length=5)
    image = models.ImageField(upload_to="images/", null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name




