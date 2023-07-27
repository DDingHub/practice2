from django.urls import path
from . import views

app_name = 'gongmo'

urlpatterns = [
    path('contest-list/', views.contest_list, name='contest_list'),
    path("contestCreate/", views.contestCreate, name="contestCreate"),
    path("<int:contestPk>/", views.contestDetail, name="contestDetail"),
    path("<int:contestPk>/contestDelete/", views.contestDelete, name="contestDelete"),
    path("<int:contestPk>/teamCreate/", views.teamCreate, name="teamCreate"),
    path("<int:contestPk>/<int:teamPk>/", views.teamDetail, name="teamDetail"),
    path("<int:contestPk>/<int:teamPk>/teamDelete/", views.teamDelete, name="teamDelete"),
    path('<int:contestPk>/<int:teamPk>/teamJoin/', views.teamJoin, name='teamJoin'),
    path('mypage/<int:user_id>/', views.mypage, name='mypage'),
    path('<int:teamPk>/bookmark/', views.bookmark, name='bookmark'),
    path('<int:teamPk>/leaveTeam/', views.leaveTeam, name='leaveTeam'),
    path('deleteNotification/<int:notification_pk>/', views.deleteNotification, name='deleteNotification'),
    path('<int:teamPk>/removeMember/', views.removeMember, name='removeMember'),
    path('approveJoinRequest/<int:notification_pk>/', views.approveJoinRequest, name='approveJoinRequest'),
    path('rejectJoinRequest/<int:notification_pk>/', views.rejectJoinRequest, name='rejectJoinRequest'),
]
