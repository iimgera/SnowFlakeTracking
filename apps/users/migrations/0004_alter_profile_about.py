# Generated by Django 4.2.1 on 2023-05-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_phone_number_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(null=True, verbose_name='Обо мне'),
        ),
    ]
