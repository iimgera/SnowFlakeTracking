from django.db import models
from datetime import time

# from apps.users.models import User


class Job(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.title


class Day(models.Model):
    date = models.DateTimeField(verbose_name='Дата')

    class Meta:
        verbose_name = 'День для проверки посещаемости'
        verbose_name_plural = 'Дни для проверки посещаемости'

    def __str__(self):
        return str(self.date)


class DayUser(models.Model):
    day = models.ForeignKey(
        Day, on_delete=models.CASCADE)
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='day_users')
    time = models.TimeField(auto_now_add=True, null=True, verbose_name='Время')
    has_reason = models.BooleanField(verbose_name='Есть причина')
    about_reason = models.TextField(
        null=True, blank=True, verbose_name='Описание причины')
    coins = models.IntegerField(default=0, verbose_name='Сноукоины')

    def __str__(self):
        return self.day

    @property
    def is_late(self):
        if self.time is None:
            if self.has_reason:
                return False
            else:
                return True
        else:
            deadline = time(14, 0)
            if self.time <= deadline:
                return False
            else:
                return True


class Fine(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()

    def __str__(self):
        return f"{self.name}: {self.size}"


class FineDayUser(models.Model):
    fine = models.ForeignKey(
        Fine, on_delete=models.CASCADE, related_name='fine_day_users')
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='days')
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='users')
    size = models.IntegerField()

    def __str__(self):
        return f"{str(self.user)}: {self.day} - {self.fine} - {self.size}"
