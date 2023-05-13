from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps
from apps.attendance.models import Fine


@receiver(post_migrate)
def create_default_fines(sender, **kwargs):
    if sender.label == 'attendance':
        Fine = apps.get_model('attendance', 'Fine')
        if not Fine.objects.exists():
            Fine.objects.create(name='Опоздание', size=50)
            Fine.objects.create(name='Неявка на работу', size=100)
            Fine.objects.create(name='Просроченный дедлайн', size=150)