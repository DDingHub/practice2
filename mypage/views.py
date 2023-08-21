from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from django.contrib.auth.models import User

class UserMyPageView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')  # POST 데이터에서 이메일을 가져옴

        try:
            user = User.objects.get(email=email)  # 이메일에 해당하는 유저를 가져옴
            user_profile = UserProfile.objects.get(user=user)  # 유저에 해당하는 프로필을 가져옴
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)

        # user_profile에서 필요한 정보들을 추출해서 response_data에 저장
        response_data = {
            "username": user_profile.user.username,
            "email": user_profile.user.email,
            "nickname": user_profile.nickname,
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
    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.filter(user=request.user).first()
        if not user_profile:
            return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)

        # Serializer 등을 사용하여 user_profile 데이터를 JSON 형태로 변환
        # ...

        return Response(serializer.data)