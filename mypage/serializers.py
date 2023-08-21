from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'name', 'jickgoon_type', 'hobbies', 'courses', 'workingTimes', 'characters', 'mbti',]
