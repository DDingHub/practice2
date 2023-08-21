from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'jickgoon_type', 'hobbies', 'courses', 'workingTimes', 'characters', 'mbti',]
