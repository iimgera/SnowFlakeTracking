from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.apps import apps

from apps.attendance.models import Fine
from apps.users.models import User, Profile


@receiver(post_migrate)
def create_default_fines(sender, **kwargs):
    if sender.label == 'attendance':
        Fine = apps.get_model('attendance', 'Fine')
        if not Fine.objects.exists():
            Fine.objects.create(name='Опоздание', size=50)
            Fine.objects.create(name='Неявка на работу', size=100)
            Fine.objects.create(name='Просроченный дедлайн', size=150)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            image=None,
            about=None,
            tg_username=None,
            job=None,
            coins=None
        )
