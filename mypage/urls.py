from django.urls import path
from .views import UserMyPageView, UserProfileJsonView

urlpatterns = [
    path('usermypage/', UserMyPageView.as_view(), name='usermypage'),
    path('user_profile_json/', UserProfileJsonView.as_view(), name='user_profile_json'),
    # 다른 URL 패턴들도 필요한 경우 추가
]
