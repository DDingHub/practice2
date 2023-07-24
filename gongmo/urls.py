from django.urls import path
from . import views

app_name = 'gongmo'

urlpatterns = [
    path('acontest-list/', views.ContestListAPIView.as_view(), name='contest_list'),
    path('contest-list/', views.contest_list, name='contest_list'),
]