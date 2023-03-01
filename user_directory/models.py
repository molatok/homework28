from django.db import models
from django.contrib.auth.models import AbstractUser


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return self.name


class Users(AbstractUser):

    ADMIN = "admin"
    USER = "user"
    MODERATOR = "moderator"

    ROLE = [(ADMIN, ADMIN), (USER, USER), (MODERATOR, MODERATOR)]

    role = models.CharField(max_length=10, choices=ROLE, default=USER)
    age = models.PositiveIntegerField(null=True)
    location = models.ManyToManyField(Location, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
