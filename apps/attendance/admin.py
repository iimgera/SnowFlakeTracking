from django.contrib import admin

from apps.attendance.models import Job, Day, DayUser, Fine, FineDayUser


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

    search_fields = ('title',)


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('id', 'date')

    search_fields = ('date',)


@admin.register(DayUser)
class DayUserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'day', 'user', 'time',
        'has_reason', 'about_reason', 'coins', 'is_late',)

    search_fields = ('user',)


@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'size', )


@admin.register(FineDayUser)
class FineDayUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'fine', 'day', 'user', 'size')

    search_fields = ('user',)
