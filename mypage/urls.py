from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)  # 엔드포인트 이름 설정
urlpatterns = router.urls
