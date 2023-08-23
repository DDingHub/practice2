from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from .forms import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#유형테스트 결과페이지
class CharacterAPIView(APIView):
    def post(self, request):
        type_id = request.data.get('typeID')
        user_id = request.user.id
        user = User.objects.filter(id=user_id).first()
        user_name = user.username
        #[[[[[[안되면 request.data.get('userID) 형식으로 해보기]]]]]]
        print(type_id)
        characters = Character.objects.filter(id=type_id)
        serializer = CharacterSerializer(characters, many=True)

        user_data = {
            'user_name' : user_name
        }

        response_data = {
            'character' : serializer.data,
            'user' : user_data
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

    # [유형추가]
    # def post(self,request):
    #     character_form = CharacterForm(request.data)
    #     if character_form.is_valid():
    #         character_form.save()
    #         return Response(character_form.cleaned_data, status=status.HTTP_201_CREATED)
    #     return Response(character_form.errors, status=status.HTTP_400_BAD_REQUEST)
    

#유형테스트 - [대표 유형으로 설정하기]
class MyCharacterAPIView(APIView):
    def post(self, request):
        type_id = request.data.get('typeID')
        user_id = request.user.id

        existing_data = MyCharacter.objects.filter(user_id=user_id, character_id=type_id).first()

        if existing_data:
            existing_data.delete()  
            response_message = "유형테스트 결과가 업데이트 되었습니다."
        else:
            my_character = MyCharacter(user_id=user_id, character_id=type_id)
            my_character.save()
            response_message = "유형테스트 결과가 저장되었습니다."

        return Response({"message": response_message}, status=status.HTTP_200_OK)