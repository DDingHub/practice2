from rest_framework import serializers
from .models import *

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = '__all__'

        
class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    dev_members = serializers.SerializerMethodField()
    plan_members = serializers.SerializerMethodField()
    design_members = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = '__all__'

    def get_dev_members(self, team):
        dev_members = team.members.filter(jickgoon='dev')
        return MemberSerializer(dev_members, many=True).data

    def get_plan_members(self, team):
        plan_members = team.members.filter(jickgoon='plan')
        return MemberSerializer(plan_members, many=True).data

    def get_design_members(self, team):
        design_members = team.members.filter(jickgoon='design')
        return MemberSerializer(design_members, many=True).data

class ScrapSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Scrap
        fields = '__all__'

class JjimSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Jjim
        fields = '__all__'