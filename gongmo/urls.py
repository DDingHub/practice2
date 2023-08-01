from django.urls import path
from . import views

app_name = 'gongmo'

urlpatterns = [
    path('acontest-list/', views.ContestListAPIView.as_view(), name='contest_list_api'),
    path("<int:contestPk>/", views.ContestDetailAPIView.as_view(), name="contestDetail"),
    path("<int:contestPk>/<int:teamPk>/", views.teamDetail, name="teamDetail"),
    path('<int:contestPk>/<int:teamPk>/teamJoin/', views.teamJoin, name='teamJoin'),
    path('mypage/<int:user_id>/', views.mypage, name='mypage'),
    path('<int:teamPk>/removeMember/', views.removeMember, name='removeMember'),
    path('approveJoinRequest/<int:notification_pk>/', views.approveJoinRequest, name='approveJoinRequest'),
    path('rejectJoinRequest/<int:notification_pk>/', views.rejectJoinRequest, name='rejectJoinRequest'),
]
