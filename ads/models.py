from django.db import models


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


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return self.name


class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


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
