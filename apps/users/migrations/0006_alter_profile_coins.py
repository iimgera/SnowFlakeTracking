# Generated by Django 4.2.1 on 2023-05-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_tg_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='coins',
            field=models.IntegerField(null=True, verbose_name='Сноукоины'),
        ),
    ]