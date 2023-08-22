from rest_framework import serializers
from .models import *


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class MyCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCharacter
        fields = '__all__'