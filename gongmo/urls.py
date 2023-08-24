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

    #교외 공모전 모음
    path('acontest-list/', views.ContestListAPIView.as_view(), name='contest_list_api'),
    #교내 공모전 모음
    path('dding-contest-list/', views.DDingContestListAPIView.as_view(), name='dding-contest_list_api'),

    #공모전 세부페이지(공모전, 팀 보여줌, 팀 생성)
    path("<int:contestPk>/", views.ContestDetailAPIView.as_view(), 
    name="contestDetail"),

    #팀 생성페이지
    path("teamCreatePage/", views.TeamCreatePageAPIView.as_view(), 
    name="teamCreatePage"),

    #팀 세부페이지(팀 지원)
    path("<int:contestPk>/<int:teamPk>/", views.TeamDetailAPIView.as_view(), name="teamDetail"),

    # MY팀(지원한 팀, 먄든 팀)
    path("myTeam/", views.MyTeamAPIView.as_view(), name="myTeam"),

    # 팀관리(지원자, 팀원 보기)
    path("teamManagement/", views.TeamManagementAPIView.as_view(), name="teamManagement"),

    #팀원 내보내기
    path("teamMemberDelete/", views.TeamMemberDeleteAPIView.as_view(), name="teamMemberDelete"),

    #팀원 수락 또는 거절
    path("teamAcceptOrReject/", views.TeamAcceptOrRejectAPIView.as_view(), name="teamAcceptOrReject"),

    # 스크랩하기
    path("scrapCreate/", views.ScrapCreateAPIView.as_view(), name="scrapCreate"),
    # 스크랩페이지
    path("scrap/", views.ScrapAPIView.as_view(), name="scrap"),
    # 찜하기
    path("jjimCreate/", views.JjimCreateAPIView.as_view(), name="jjimCreate"),
    # 찜페이지
    path("jjim/", views.JjimAPIView.as_view(), name="jjim"),

    #알림보기
    path("notification/", views.NotificationListAPIView.as_view(), name="notification"),

    #[[[[[[userInfo필요한지 확인]]]]]]
    #유저정보넣기
    path('userInfo/',views.UserInfoAPIView.as_view(), name='userInfo'),
]