from rest_framework import serializers
from .models import *

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = '__all__'

class JickgoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jickgoon
        fields = '__all__'
        
class TeamSerializer(serializers.ModelSerializer):
    jickgoons = JickgoonSerializer(many=True)
    class Meta:
        model = Team
        fields = '__all__'
