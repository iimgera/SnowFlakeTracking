from rest_framework import serializers

from apps.attendance.models import Job, Day, DayUser, Fine, FineDayUser


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'title')


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'date')


class DayUserSerializer(serializers.ModelSerializer):
    is_late = serializers.BooleanField(read_only=True)

    class Meta:
        model = DayUser
        fields = (
            'id', 'day', 'user', 'time',
            'has_reason', 'about_reason', 'coins', 'is_late', )


class FineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fine
        fields = ('id', 'name', 'size',)


class FineDayUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FineDayUser
        fields = ('id', 'fine', 'day', 'user', 'size', )
