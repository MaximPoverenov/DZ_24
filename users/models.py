from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

NULLABLE = {"blank": True, "null": True}


class Users(AbstractUser):
    username = None  # Убираем поле username
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Электронная почта"
    )

    phone_number = PhoneNumberField(
        unique=True,
        verbose_name="Телефон",
        help_text="Введите номер телефона",
        **NULLABLE,
    )
    country = CountryField(
        verbose_name="Город",
        **NULLABLE,
        help_text="Город проживания",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        **NULLABLE,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )

    token = models.CharField(max_length=100, verbose_name="Токен", **NULLABLE)
    city = models.CharField(max_length=100, verbose_name="Город", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
