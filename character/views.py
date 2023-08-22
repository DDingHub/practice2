from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from .forms import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#유형테스트 목록, 유형테스트 등록(db삭제될까봐 만듦)
class CharacterAPIView(APIView):
    # def get(self,request):
    #     type_id = request.data.get('typeId')
    #     characters = Character.objects.filter(id=type_id)
    #     serializer = CharacterSerializer(characters, many=True)
    #     return Response(serializer.data)
    def post(self, request):
        type_id = request.data.get('typeId')
        characters = Character.objects.filter(id=type_id)
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    # [유형추가]
    # def post(self,request):
    #     character_form = CharacterForm(request.data)
    #     if character_form.is_valid():
    #         character_form.save()
    #         return Response(character_form.cleaned_data, status=status.HTTP_201_CREATED)
    #     return Response(character_form.errors, status=status.HTTP_400_BAD_REQUEST)
    
#유형테스트 결과 유저한테 보내줌
class MyCharacterAPIView(APIView):
    def get(self, request):
        user = request.user
        my_characters = MyCharacter.objects.filter(user=user)
        serialized_characters = []

        for my_character in my_characters:
            serialized_characters.append(CharacterSerializer(my_character.character).data)

        return Response(serialized_characters)
    def post(self, request):
        user = request.user
        character_id = request.data.get('character_id')

        if character_id:
            character = get_object_or_404(Character, pk=character_id)
            my_character, created = MyCharacter.objects.get_or_create(user=user, character=character)

            if created:
                return Response({"message": "Character assigned successfully."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Character already assigned to the user."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "character_id is required."}, status=status.HTTP_400_BAD_REQUEST)