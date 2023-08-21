from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from django.contrib.auth.models import User

class UserMyPageView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')  # POST 데이터에서 username을 가져옴

        try:
            user = User.objects.get(username=username)  # username에 해당하는 유저 가져옴
            user_profile = UserProfile.objects.get(user=user)  # 해당 유저에 대한 프로필 정보 가져옴
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)

        # user_profile에서 필요한 정보들을 추출해서 response_data에 저장
        response_data = {
            "username": user_profile.user.username,
            "email": user_profile.user.email,
            "name": user_profile.name,
            # 다른 필드들도 필요한 만큼 추가
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