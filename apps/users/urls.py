from django.urls import path, include

from apps.users import views
from rest_framework import routers

app_name = 'users'


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
