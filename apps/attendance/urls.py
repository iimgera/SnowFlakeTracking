from django.urls import path

from apps.attendance import views

app_name = 'attendance'

urlpatterns = [
    path('jobs/', views.JobListCreateAPIView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', views.JobRetrieveUpdateDestroyAPIView.as_view(), name='job-retrieve-update-destroy'),
    path('days/', views.DayListCreateAPIView.as_view(), name='day-list-create'),
    path('days/<int:pk>/', views.DayRetrieveUpdateDestroyAPIView.as_view(), name='day-retrieve-update-destroy'),
    path('day_user/', views.DayUserListCreateAPIView.as_view(), name='day-user-list-create'),
    path('day_user/<int:pk>/', views.DayUserRetrieveUpdateDestroyAPIView.as_view(), name='day-user-retrieve-update-destroy'),
    path('fines/', views.FineListCreateAPIView.as_view(), name='fine-list-create'),
    path('fines/<int:pk>/', views.FineRetrieveUpdateDestroyAPIView.as_view(), name='fine-retrieve-update-destroy'),
    path('fine_day_user/', views.FineDayUserListAPIView.as_view(), name='fine-day-user-list'),
    path('fine_day_user/create', views.FineDayUserCreateAPIView.as_view(), name='fine-day-user-create'),
    path('fine_day_user/<int:pk>/', views.FineDayUserRetrieveUpdateDestroyAPIView.as_view(), name='fine-day-user-retrieve-update-destroy'),
]
