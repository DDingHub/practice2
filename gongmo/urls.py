from django.urls import path
from . import views

app_name = 'gongmo'

urlpatterns = [
    path('api/contest-list/', views.ContestListAPIView.as_view(), name='contest_list_api'),
]
