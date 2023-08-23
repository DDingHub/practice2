from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'nickname', 'major', 'job', 'hobby', 'dream', 'tendency_worktime', 'tendency_personality', 'tendency_MBTI', 'languages_tools', 'call', 'introduce', 'portfolio', 'user_type', 'type_message']
