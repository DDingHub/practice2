from rest_framework import serializers
from .models import *

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    major = models.CharField(max_length=100)
    job = models.TextField()  # 이 부분은 나중에 정확한 필드 타입을 선택해야 합니다.
    hobby = models.TextField()  # 이 부분도 필드 타입을 선택해야 합니다.
    dream = models.TextField()  # 이 부분도 필드 타입을 선택해야 합니다.
    tendency_worktime = models.CharField(max_length=20)
    tendency_personality = models.TextField()  # 이 부분도 필드 타입을 선택해야 합니다.
    tendency_MBTI = models.CharField(max_length=10)
    languages_tools = models.TextField()
    call = models.TextField()
    introduce = models.TextField()
    portfolio = models.TextField()
    user_type = models.TextField()
    type_message = models.TextField()

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

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    job = serializers.ListField(child=serializers.CharField())
    hobby = serializers.ListField(child=serializers.CharField())
    dream = serializers.ListField(child=serializers.CharField())
    tendency_worktime = serializers.CharField()
    tendency_personality = serializers.ListField(child=serializers.CharField())
    tendency_MBTI = serializers.CharField(max_length=10)
    languages_tools = serializers.ListField(child=serializers.CharField())
    call = serializers.CharField()
    introduce = serializers.CharField()
    portfolio = serializers.CharField()
    user_type = serializers.CharField()
    type_message = serializers.CharField()
    nickname = serializers.CharField()
    major = serializers.CharField()  # 'major' 필드 추가

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'job', 'hobby', 'dream', 'tendency_worktime', 'tendency_personality', 'tendency_MBTI', 'languages_tools', 'call', 'introduce', 'portfolio', 'user_type', 'type_message', 'nickname', 'major']  # 'major' 필드 추가

    def create(self, validated_data):
        job = validated_data.pop('job')
        hobby = validated_data.pop('hobby')
        dream = validated_data.pop('dream')
        tendency_personality = validated_data.pop('tendency_personality')
        tendency_MBTI = validated_data.pop('tendency_MBTI')
        languages_tools = validated_data.pop('languages_tools')
        call = validated_data.pop('call')
        introduce = validated_data.pop('introduce')
        portfolio = validated_data.pop('portfolio')
        user_type = validated_data.pop('user_type')
        type_message = validated_data.pop('type_message')
        nickname = validated_data.pop('nickname')
        major = validated_data.pop('major')  # 'major' 필드 추출
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # 사용자의 추가 정보를 생성 및 저장하는 코드
        UserProfile.objects.create(
            user=user,
            nickname=nickname,
            major=major,  # 'major' 필드 추가
            job=job,
            hobby=hobby,
            dream=dream,
            tendency_worktime=validated_data['tendency_worktime'],
            tendency_personality=tendency_personality,
            tendency_MBTI=tendency_MBTI,
            languages_tools=languages_tools,
            call=call,
            introduce=introduce,
            portfolio=portfolio,
            user_type=user_type,
            type_message=type_message
        )
        
        return user


    
class JjimSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Jjim
        fields = '__all__'

class Notification(models.Model):
    # Notification 모델 필드들 정의
    pass

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
        

class UserInfoSerializer(serializers.ModelSerializer):
    job = serializers.ListField(child=serializers.CharField())
    hobby = serializers.ListField(child=serializers.CharField())
    dream = serializers.ListField(child=serializers.CharField())
    tendency_personality = serializers.ListField(child=serializers.CharField())
    
    class Meta:
        model = UserInfo
        fields = '__all__'