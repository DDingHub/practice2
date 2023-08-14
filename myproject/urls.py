from django.contrib import admin
from django.urls import include, path
from gongmo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gongmo.urls')),
    path('api/', include('mypage.urls')),
]