from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from mypage.models import UserProfile  # mypage 앱의 UserProfile 모델을 임포트

class UserMyPageView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")

        if not email:
            return Response({"message": "이메일을 제공해야 합니다."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            user_profile = user.user_profile
        except User.DoesNotExist:
            return Response({"message": "해당 이메일로 연결된 사용자를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        except UserProfile.DoesNotExist:
            return Response({"message": "사용자 프로필을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        response_data = {
            "email": user.email,
            "nickname": user.username,
            "major": user_profile.major,
            "job": user_profile.job,
            "hobby": user_profile.hobby,
            "dream": user_profile.dream,
            "tendency_worktime": user_profile.tendency_worktime,
            "tendency_personality": user_profile.tendency_personality,
            "tendency_MBTI": user_profile.tendency_MBTI,
            "languages_tools": user_profile.languages_tools,
            "call": user_profile.call,
            "introduce": user_profile.introduce,
            "portfolio": user_profile.portfolio,
            "user_type": user_profile.user_type,
            "type_message": user_profile.type_message,
        }

        return Response(response_data, status=status.HTTP_200_OK)

class UserProfileJsonView(APIView):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.filter(user=request.user).first()
        if not user_profile:
            return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializer(user_profile)  # 시리얼라이저로 데이터 변환
        return Response(serializer.data)
