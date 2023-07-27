from django.urls import path
from . import views

app_name = 'gongmo'

urlpatterns = [
    path('contest-list/', views.contest_list, name='contest_list'),
]
