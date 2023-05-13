from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from apps.attendance.models import Job


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=100, verbose_name='Имя пользователя')
    full_name = models.CharField(max_length=150, verbose_name='Полное имя')
    date_registered = models.DateField(
        auto_now_add=True, verbose_name='Дата регистрации')
    phone_number = models.CharField(max_length=50, verbose_name='Номер телефона')
    email = models.EmailField(max_length=60, unique=True, verbose_name='Почта')

    is_admin = models.BooleanField(
        verbose_name='Является ли пользователь админом',
        default=False,
    )

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField(
        upload_to='profiles/%Y/%m/%d/', verbose_name='Изображение')
    about = models.TextField(verbose_name='Обо мне')
    phone_number = models.CharField(
        max_length=50, verbose_name='Номер телефона')
    tg_username = models.CharField(
        max_length=100, verbose_name='Никнейм в телеграм')
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name='profiles')
    coins = models.IntegerField(verbose_name='Сноукоины')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return str(self.user)
