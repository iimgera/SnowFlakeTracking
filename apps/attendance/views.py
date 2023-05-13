from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from apps.attendance.models import Job, Day, DayUser, Fine, FineDayUser
from apps.attendance.serializers import (
    JobSerializer, DaySerializer, DayUserSerializer,
    FineSerializer, FineDayUserSerializer)


def get_user_object(request):
    user = request.user
    if user.is_authenticated:
        return user
    raise PermissionDenied()


class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAdminUser, ]


class JobRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAdminUser, ]


class DayListCreateAPIView(generics.ListCreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    permission_classes = [permissions.IsAdminUser, ]


class DayRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    permission_classes = [permissions.IsAdminUser, ]


class DayUserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DayUserSerializer
    permission_classes = [permissions.IsAdminUser, ]

    def get_queryset(self):
        user = get_user_object(self.request)
        queryset = DayUser.objects.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        user = get_user_object(self.request)
        serializer.save(user=user)


class DayUserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DayUser.objects.all()
    serializer_class = DayUserSerializer
    permission_classes = [permissions.IsAdminUser, ]

    def get_object(self):
        user = get_user_object(self.request)
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, user=user, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj


class FineListCreateAPIView(generics.ListCreateAPIView):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer
    permission_classes = [permissions.IsAdminUser, ]


class FineRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer
    permission_classes = [permissions.IsAdminUser, ]


class FineDayUserCreateAPIView(generics.CreateAPIView):
    queryset = FineDayUser.objects.all()
    serializer_class = FineDayUserSerializer
    permission_classes = [permissions.IsAdminUser, ]


class FineDayUserListAPIView(generics.ListAPIView):
    serializer_class = FineDayUserSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        user = get_user_object(self.request)
        queryset = FineDayUser.objects.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        user = get_user_object(self.request)
        serializer.save(user=user)


class FineDayUserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FineDayUser.objects.all()
    serializer_class = FineDayUserSerializer
    permission_classes = [permissions.IsAdminUser, ]

    def get_object(self):
        user = get_user_object(self.request)
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, user=user, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        self.check_object_permissions(self.request, obj)
        self.check_object_permissions(self.request, obj)
        return obj
