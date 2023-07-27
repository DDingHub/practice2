from django.urls import path
from . import views

app_name = 'gongmo'

urlpatterns = [
<<<<<<< HEAD
    path('contest-list/', views.ContestListAPIView.as_view(), name='contest_list'),
]
=======
    path('acontest-list/', views.ContestListAPIView.as_view(), name='contest_list'),
    path('contest-list/', views.contest_list, name='contest_list'),
]
>>>>>>> a794b70ea1f98f9965768be7cf04e8c6a0b98054
