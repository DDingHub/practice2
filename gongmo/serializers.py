from rest_framework import serializers
from .models import Contest

from rest_framework import serializers
from .models import Contest, Team, Member, Jickgoon

class JickgoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jickgoon
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    jickgoon = JickgoonSerializer()
    class Meta:
        model = Member
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True)
    class Meta:
        model = Team
        fields = '__all__'

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = '__all__'

class ContestDetailSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True)
    class Meta:
        model = Contest
        fields = '__all__'