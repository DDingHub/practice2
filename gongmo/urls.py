from django.urls import path
from . import views

app_name = 'gongmo'

urlpatterns = [
    #회원가입
    path("signup/", views.SignUpAPIView.as_view(), name="signup"),
    #로그인
    path("login/", views.LoginAPIView.as_view(), name="login"),
    #로그아웃
    path("logout/", views.LogoutAPIView.as_view(), name="logout"),
    #공모전 모음
    path('acontest-list/', views.ContestListAPIView.as_view(), 
    name='contest_list_api'),
    #공모전 세부페이지(공모전, 팀 보여줌)
    path("<int:contestPk>/", views.ContestDetailAPIView.as_view(), name="contestDetail"),
    #팀 세부페이지(팀 지원)
    path("<int:contestPk>/<int:teamPk>/<int:jickgoonPk>", views.TeamDetailAPIView.as_view(), name="teamDetail"),
    # path('mypage/<int:user_id>/', views.mypage, name='mypage'),
    # path('<int:teamPk>/removeMember/', views.removeMember, name='removeMember'),
    # path('approveJoinRequest/<int:notification_pk>/', views.approveJoinRequest, name='approveJoinRequest'),
    # path('rejectJoinRequest/<int:notification_pk>/', views.rejectJoinRequest, name='rejectJoinRequest'),
]
