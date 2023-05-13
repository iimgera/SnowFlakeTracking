from django.contrib import admin
from apps.users.models import User, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
            'username', 'full_name',
            'date_registered', 'phone_number',
            'email', 'is_admin', )

    search_fields = ('username',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
            'id', 'user', 'image',
            'about', 'phone_number',
            'tg_username', 'job', 'coins', )

    search_fields = ('tg_username',)
