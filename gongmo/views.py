from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
import re
import requests
import datetime
import jwt
from django.conf import settings
from bs4 import BeautifulSoup
from django.contrib import messages
from django.urls import reverse
from django.utils.html import escape
from django.utils import timezone
from django.http import HttpResponseForbidden
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import PermissionDenied
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime,timedelta
from mypage.models import UserProfile
from .serializers import SignupSerializer
from rest_framework.authtoken.models import Token
from .serializers import SignupSerializer


def generate_jwt_token(user):
    secret_key = settings.SECRET_KEY  # 시크릿 키 설정
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(days=1)  # 1일 후 만료

    payload = {
        'user_id': user.id,
        'exp': expiration_time,
    }

    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def save_contest_data():
    url = "https://www.wevity.com/?c=find&s=1&gub=1&cidx=20&gp="
    for pageNum in range(1, 2):
        response = requests.get(url + str(pageNum))
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        wholeHtml = soup.find_all(class_="list")

        for tag in wholeHtml:
            for a_tag in tag:
                match = re.search(r'href="([^"]+)"', str(a_tag))
                if match:
                    href = "https://www.wevity.com/" + match.group(1)
                    href = href[-5:]
                    pageUrl = 'https://www.wevity.com/?c=find&s=1&gub=1&cidx=20&gbn=viewok&gp=1&ix=' + href

                    response2 = requests.get(pageUrl)
                    html_content2 = response2.text
                    soup2 = BeautifulSoup(html_content2, "html.parser")
                    dicttt = {}

                    h6_element = soup2.find("h6", class_="tit")
                    if h6_element:
                        dicttt['제목'] = h6_element.text

                    div_element = soup2.find(class_='thumb')
                    if div_element:
                        img_element = div_element.find('img')
                        if img_element:
                            src = img_element['src']
                            dicttt['사진'] = "https://www.wevity.com/" + src
                  
                    ul = soup2.find("ul", {"class": "cd-info-list"})
                    li = ul.select('li')

                    for i in range(8):
                        soup3 = BeautifulSoup(str(li[i]), 'html.parser')
                        span_element3 = soup3.find('span', class_='tit')
                        li_element3 = soup3.find('li')
                        if span_element3 and li_element3:
                            keyy = span_element3.text
                            field_text3 = li_element3.get_text(strip=True)
                            field_list3 = field_text3.split(keyy)[1].split(',')
                            fields4 = ', '.join([field.strip() for field in field_list3])
                            dicttt[keyy] = fields4

                    # 상세정보 추가
                    comm_desc_element = soup2.find("div", class_="comm-desc")
                    if comm_desc_element:
                        comm_desc_text = comm_desc_element.text.strip()
                        if isinstance(comm_desc_text, list):
                            comm_desc_text = ' '.join(comm_desc_text)
                        dicttt['상세정보'] = comm_desc_text

                    # 조회수(인기순) 추가
                    read_span = soup2.find("span", class_="read")
                    if read_span:
                        read_text = read_span.get_text(strip=True)
                        if "조회수 :" in read_text:
                            view_text = read_text.split("조회수 :")[1]
                            views = int(view_text.replace(',', '').strip())
                            dicttt['조회수'] = views

                    # 중복된 데이터 검사 및 제거
                    if Contest.objects.filter(title=dicttt.get('제목')).exists():
                        continue  # 이미 저장된 제목인 경우 건너뜁니다.
                    else:
                        contest = Contest.objects.create(
                            title=dicttt.get('제목'),
                            photo=dicttt.get('사진'),
                            field=dicttt.get('분야'),
                            eligibility=dicttt.get('응모대상'),
                            organizer=dicttt.get('주최/주관'),
                            sponsorship=dicttt.get('후원/협찬'),
                            application_period=dicttt.get('접수기간'),
                            prize_total=dicttt.get('총 상금'),
                            prize_first=dicttt.get('1등 상금'),
                            website=dicttt.get('홈페이지'),
                            details=dicttt.get('상세정보'),
                            registration_date=datetime.now(),
                            viewCount = dicttt.get('조회수')
                        )
                        contest.save()

# 날짜변환 함수
def parse_application_period(application_period):
    parts = application_period.split("~")
    end_date = parts[1].split("D")[0].strip() 
    return end_date

#공모전 목록 보여주기
class ContestListAPIView(APIView):
    ##[[[[[[put으로 필터링 하고 있는데 더 생각해보기]]]]]]
    def get(self, request):
        # save_contest_data()
        order_by = request.data.get("order_by")
        user = request.user.id

        if order_by == "viewCount":
            contests = Contest.objects.filter(isSchool=False).order_by('-viewCount')
        elif order_by == "application_period":
            contests = Contest.objects.filter(isSchool=False)
            contests = sorted(contests, key=lambda contest: parse_application_period(contest.application_period), reverse=True)
        else:
            contests = Contest.objects.filter(isSchool=False).order_by('registration_date')

        user_scrapped_contests = Scrap.objects.filter(user=user).values_list('contest_id', flat=True)

        contest_data = []
        for contest in contests:
            serialized_contest = ContestSerializer(contest).data
            serialized_contest["is_scrapped"] = contest.id in user_scrapped_contests

            team_count = Team.objects.filter(contest=contest).count()
            serialized_contest["team_count"] = team_count

            contest_data.append(serialized_contest)

        return Response(contest_data)
    def put(self, request):
        return self.get(request)

#교내 공모전 목록
class DDingContestListAPIView(APIView):
    def get(self, request):
        dding_contests = Contest.objects.filter(isSchool=True)
        serializer = ContestSerializer(dding_contests, many=True)
        return Response(serializer.data)

    # def post(self,request):
    #     dding_contest_form = DDingContestForm(request.data)
    #     if dding_contest_form.is_valid():
    #         dding_contest_form.save()
    #         return Response(dding_contest_form.cleaned_data, status=status.HTTP_201_CREATED)
    #     return Response(dding_contest_form.errors, status=status.HTTP_400_BAD_REQUEST)

#공모전 세부페이지
class ContestDetailAPIView(APIView):
    #공모전 정보와 팀 정보 가져오기
    def get(self, request, contestPk):
        user = request.user.id
        contest = get_object_or_404(Contest, pk=contestPk)
        teams = Team.objects.filter(contest=contest)

        user_scrapped_contests = Scrap.objects.filter(user=user).values_list('contest_id', flat=True)
        contest_data = []
        serialized_contest = ContestSerializer(contest).data
        serialized_contest["is_scrapped"] = contest.id in user_scrapped_contests
        contest_data.append(serialized_contest)

        user_jjim_teams = Jjim.objects.filter(user=user).values_list('team_id', flat=True)
        team_data = []
        for team in teams:
            serialized_team = TeamSerializer(team).data
            serialized_team["is_jjim"] = team.id in user_jjim_teams

            for member in team.members.all():
                member_data = {
                    "id": member.id,
                    "jickgoon": member.jickgoon,
                    "team": member.team.id,
                    "user": member.user.id,
                    "crown": member.user.id == team.created_by.id
                }
                serialized_team[member.jickgoon + "_members"] = [member_data]

            team_data.append(serialized_team)

        return Response({'contest': contest_data, 'teams': team_data})
    #팀 생성하기
    def post(self, request, contestPk):
        contest = get_object_or_404(Contest, pk=contestPk)
        team_form = TeamForm(request.data)

        if team_form.is_valid():
            leaderJickgoon = request.data.get('leaderJickgoon')
            team = team_form.save(commit=False)
            team.contest = contest
            team.created_by = request.user
            #[[[[[tendency수정필요]]]]]
            team.save()

            Member.objects.create(team=team, user=request.user, jickgoon=leaderJickgoon)    

            if leaderJickgoon == 'dev':
              team.dev += 1
            elif leaderJickgoon == 'plan':
                team.plan += 1
            elif leaderJickgoon == 'design':
                team.design += 1

            team.save()

            response_data = {
                "message": "팀이 생성되었습니다.",
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            errors = {}
            errors.update(team_form.errors)
            return Response({'error': errors}, status=status.HTTP_400_BAD_REQUEST)

#팀 세부페이지
class TeamDetailAPIView(APIView):
    #팀 세부페이지 가져오기
    def get(self, request, teamPk, contestPk):
        user = request.user.id
        team = get_object_or_404(Team, pk=teamPk)

        user_jjim_teams = Jjim.objects.filter(user=user).values_list('team_id', flat=True)
        jjim_data=[]
        serialized_team = TeamSerializer(team).data
        serialized_team["is_jjim"] = team.id in user_jjim_teams
        for member in team.members.all():
            member_data = {
                "id": member.id,
                "jickgoon": member.jickgoon,
                "team": member.team.id,
                "user": member.user.id,
                "crown": member.user.id == team.created_by.id
            }
            if member.jickgoon == "dev":
                serialized_team["dev_members"] = [member_data]
            elif member.jickgoon == "plan":
                serialized_team["plan_members"] = [member_data]
            elif member.jickgoon == "design":
                serialized_team["design_members"] = [member_data]

        serialized_team["member_count"] = team.members.count() 
        jjim_data.append(serialized_team)
        return Response(jjim_data)

    #팀 지원하기
    def post(self, request, teamPk, contestPk):
        team = get_object_or_404(Team, pk=teamPk)
        jickgoon_type = request.data.get("jickgoon_type")


        if jickgoon_type not in ['dev', 'plan', 'design']:
            return Response({"error": "유효하지 않은 직군입니다."},
                            status=status.HTTP_400_BAD_REQUEST)
        
        if jickgoon_type == "dev" and team.dev >= team.dev_capacity:
            return Response({"error": "이미 꽉찬 직군입니다."},
                            status=status.HTTP_400_BAD_REQUEST)
        elif jickgoon_type == "plan" and team.plan >= team.plan_capacity:
            return Response({"error": "이미 꽉찬 직군입니다."},
                            status=status.HTTP_400_BAD_REQUEST)
        elif jickgoon_type == "design" and team.design >= team.design_capacity:
            return Response({"error": "이미 꽉찬 직군입니다."},
                            status=status.HTTP_400_BAD_REQUEST)
        
        application = Application.objects.create(team=team, applicant=request.user, jickgoon=jickgoon_type)

        if team.created_by != request.user:
            notification_message = f"{request.user.username}님 {team.name}의 팀원이 되고 싶어해요!"
            Notification.objects.create(user=team.created_by, message=notification_message, type="팀원 할래요")

        return Response({"message": "팀 지원이 완료되었습니다. 팀장의 승인을 기다려주세요."},status=status.HTTP_201_CREATED)

        #팀 수정하기
    def put(self, request, contestPk, teamPk):
        contest = get_object_or_404(Contest, pk=contestPk)
        team = get_object_or_404(Team, pk=teamPk)
        team_form = TeamForm(request.data, instance=team)

        if team_form.is_valid():
            updated_team = team_form.save(commit=False)
            updated_team.contest = contest
            updated_team.created_by = request.user.id
            updated_team.tendency = json.dumps(request.data.get('tendency'))
            updated_team.save()

            response_data = {
                "message": "팀이 수정되었습니다.",
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            errors = {}
            errors.update(team_form.errors)
            return Response({'error': errors}, status=status.HTTP_400_BAD_REQUEST)
        
# 회원가입
class SignUpAPIView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # 사용자의 추가 정보를 생성 및 저장하는 코드
            UserProfile.objects.create(
                user=user,
                nickname=serializer.validated_data['nickname'],
                major=serializer.validated_data['major'],
                job=serializer.validated_data['job'],
                hobby=serializer.validated_data['hobby'],
                dream=serializer.validated_data['dream'],
                tendency_worktime=serializer.validated_data['tendency_worktime'],
                tendency_personality=serializer.validated_data['tendency_personality'],
                tendency_MBTI=serializer.validated_data['tendency_MBTI'],
                languages_tools=serializer.validated_data['languages_tools'],
                call=serializer.validated_data['call'],
                introduce=serializer.validated_data['introduce'],
                portfolio=serializer.validated_data['portfolio'],
                user_type=serializer.validated_data['user_type'],
                type_message=serializer.validated_data['type_message']
            )

            return Response({'message': '회원가입이 완료되었습니다.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': '사용자 이름과 비밀번호를 입력해주세요.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': '잘못된 사용자 이름 또는 비밀번호입니다.'}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)

        # Token 생성
        token = generate_jwt_token(user)

        user_data = {
            "id": user.id,
            "username": user.username
        }
        
        response_data = {
            "message": "로그인 완료.",
            "user": user_data,
            "access": token  # 생성된 토큰 값을 응답에 포함
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)
# 로그아웃
class LogoutAPIView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({'message': '로그아웃되었습니다.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': '로그인되어 있지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

#My팀 보기(지원한 팀, 만든 팀)
class MyTeamAPIView(APIView):
    def get(self, request):
        userPk = 1 #request로 수정

        #내가 지원한 팀 - 응답 대기
        applications = Application.objects.filter(applicant=userPk, is_approved=False)
        responseWait_team_ids = applications.values_list('team', flat=True)
        teams_responseWait = Team.objects.filter(id__in=responseWait_team_ids)
        teams_responseWait_data = []
        for team in teams_responseWait:
            application = applications.get(team=team)
            team_data = TeamSerializer(team).data
            team_data['applyJickgoon'] = application.jickgoon
            team_data['contest_title'] = team.contest.title

            jjim_exists = Jjim.objects.filter(user=request.user, team=team).exists()
            team_data['is_jjim'] = jjim_exists

            for dev_member in team_data['dev_members']:
                if dev_member['user'] == team_data['created_by']:
                    dev_member['crown'] = True
                else:
                    dev_member['crown'] = False
                    
            for plan_member in team_data['plan_members']:
                if plan_member['user'] == team_data['created_by']:
                    plan_member['crown'] = True
                else:
                    plan_member['crown'] = False
                    
            for design_member in team_data['design_members']:
                if design_member['user'] == team_data['created_by']:
                    design_member['crown'] = True
                else:
                    design_member['crown'] = False
            teams_responseWait_data.append(team_data)
            

        #내가 지원한 팀 - 수락됨
        teams_joined = Team.objects.filter(members__user=userPk)
        teams_accepted = teams_joined.exclude(created_by=userPk)
        teams_accepted_serializer = TeamSerializer(teams_accepted, many=True)
        teams_accepted_data = teams_accepted_serializer.data
        for team in teams_accepted_data:
            contest_id = team['contest']
            contest = Contest.objects.get(id=contest_id)
            team['contest_title'] = contest.title
            for dev_member in team['dev_members']:
                if dev_member['user'] == team['created_by']:
                    dev_member['crown'] = True
                else:
                    dev_member['crown'] = False
                    
            for plan_member in team['plan_members']:
                if plan_member['user'] == team['created_by']:
                    plan_member['crown'] = True
                else:
                    plan_member['crown'] = False
                    
            for design_member in team['design_members']:
                if design_member['user'] == team['created_by']:
                    design_member['crown'] = True
                else:
                    design_member['crown'] = False
            
            jjim_exists = Jjim.objects.filter(user=request.user, team_id=team['id']).exists()
            team['is_jjim'] = jjim_exists

        #내가 지원한 팀 - 거절됨
        teams_rejected = RejectedTeam.objects.filter(user=userPk)
        rejected_team_ids = teams_rejected.values_list('team', flat=True)
        teams_rejected_info = Team.objects.filter(id__in=rejected_team_ids)
        teams_rejected_serializer = TeamSerializer(teams_rejected_info, many=True)
        teams_rejected_data = teams_rejected_serializer.data
        for team in teams_rejected_data:
            contest_id = team['contest']
            contest = Contest.objects.get(id=contest_id)
            team['contest_title'] = contest.title
            for dev_member in team['dev_members']:
                if dev_member['user'] == team['created_by']:
                    dev_member['crown'] = True
                else:
                    dev_member['crown'] = False
                    
            for plan_member in team['plan_members']:
                if plan_member['user'] == team['created_by']:
                    plan_member['crown'] = True
                else:
                    plan_member['crown'] = False
                    
            for design_member in team['design_members']:
                if design_member['user'] == team['created_by']:
                    design_member['crown'] = True
                else:
                    design_member['crown'] = False

            jjim_exists = Jjim.objects.filter(user=request.user, team_id=team['id']).exists()
            team['is_jjim'] = jjim_exists

        #내가 만든 팀
        teams_created = Team.objects.filter(created_by=userPk)
        teams_created_serializer = TeamSerializer(teams_created, many=True)
        teams_created_data = teams_created_serializer.data
        for team in teams_created_data:
            dev_capacity = team.get('dev_capacity', 0)
            plan_capacity = team.get('plan_capacity', 0)
            design_capacity = team.get('design_capacity', 0)
            dev_joined = team.get('dev', 0)
            plan_joined = team.get('plan', 0)
            design_joined = team.get('design', 0)
            team['applicant_count'] = Application.objects.filter(team=team['id'], is_approved=False).count()
            team['member_count'] = dev_joined + plan_joined + design_joined 
            if dev_capacity == dev_joined and plan_capacity == plan_joined and design_capacity == design_joined:
                team['isfull'] = True
            else:
                team['isfull'] = False

            for dev_member in team['dev_members']:
                if dev_member['user'] == team['created_by']:
                    dev_member['crown'] = True
                else:
                    dev_member['crown'] = False
                    
            for plan_member in team['plan_members']:
                if plan_member['user'] == team['created_by']:

                    plan_member['crown'] = True
                else:
                    plan_member['crown'] = False
                    
            for design_member in team['design_members']:
                if design_member['user'] == team['created_by']:
                    design_member['crown'] = True
                else:
                    design_member['crown'] = False

            contest_id = team['contest']
            contest = Contest.objects.get(id=contest_id)
            team['contest_title'] = contest.title

        responseWait_team_count = len(teams_responseWait_data)
        accepted_team_count = len(teams_accepted_data)
        rejected_team_count = len(teams_rejected_data)

        applied_count = (responseWait_team_count + accepted_team_count + rejected_team_count)
        created_team_count = len(teams_created_data)

        applied = {
            "responseWaitTeam": teams_responseWait_data,
            "acceptedTeam": teams_accepted_data,
            "rejectedTeam": teams_rejected_data,
            "team_count" : applied_count
        }

        created = {
            "createdTeam" : teams_created_data,
            "team_count" : created_team_count
        }


        return Response({
            "applied": applied,
            "created": created
            }, status=status.HTTP_200_OK)

# 팀 - 지원자, 팀원 가져오기
class TeamManagementAPIView(APIView):
    # 내 팀에 신청한 사람 가져오기
    def post(self, request):
        userPk = request.user.id
        user = get_object_or_404(User, pk=userPk)

        team_id = request.data.get('team')
        team = get_object_or_404(Team, pk=team_id)

        if team.created_by == user:
            team_info = {
                'id': team.id,
                'teamname': team.teamname
            }

            responseWait = Application.objects.filter(team=team, is_approved=False)
            responseWait_data = []
            for wait in responseWait:
                wait_data = {
                    'user_id': wait.applicant.id,
                    'username': wait.applicant.username,
                    'jickgoon': wait.jickgoon
                }
                responseWait_data.append(wait_data)

            members_data = []
            for member in team.members.exclude(user=team.created_by):
                member_data = {
                    'user_id': member.user.id,
                    'username': member.user.username,
                    'jickgoon': member.jickgoon
                }
                members_data.append(member_data)

            response_data = {
                'team_info': team_info,
                'responseWait': responseWait_data,
                'accepted' : members_data,
                'total_responseWait': len(responseWait_data),
                'total_accepted' : len(members_data),
                'total_count' : len(members_data) + len(responseWait_data)
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            raise PermissionDenied("You don't have permission to view this team.")

# 팀원 삭제
class TeamMemberDeleteAPIView(APIView):
    # 내 팀에 들어와 있는 사람 내보내기
    def post(self, request):
        userPk = request.user.id
        user = get_object_or_404(User, pk=userPk)
        team_id = request.data.get("team")
        user_id = request.data.get("user")

        try:
            team = get_object_or_404(Team, id=team_id, created_by=user)
            member = get_object_or_404(Member, user=user_id, team=team)
            member.delete()
            return Response({"message": "멤버가 팀에서 내보내졌습니다."}, status=status.HTTP_200_OK)
        except Team.DoesNotExist:
            return Response({"message": "팀이 존재하지 않거나 권한이 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        except Member.DoesNotExist:
            return Response({"message": "멤버가 존재하지 않거나 팀에 속해 있지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# 지원자 수락 또는 거절
class TeamAcceptOrRejectAPIView(APIView):
    def post(self, request):
        userPk = request.user.id
        user = get_object_or_404(User, pk=userPk)
        applicantion_id = request.data.get("applicantion_id")
        is_approved = request.data.get("is_approved")

        application = get_object_or_404(Application, id=applicantion_id, team__created_by=user)

        if is_approved == "true":
            application.is_approved = True
            application.save()
            applicant = application.applicant
            team = application.team
            notification_message = f"{team.name} 팀에서 팀 요청을 수락했어요!"
            Notification.objects.create(user=applicant, message=notification_message, type="요청 결과")

            if application.jickgoon == 'dev':
              team.dev += 1
            elif application.jickgoon == 'plan':
                team.plan += 1
            elif application.jickgoon == 'design':
                team.design += 1
            
            team.save()

            Member.objects.create(team=application.team, user=application.applicant, jickgoon=application.jickgoon)
            application.delete()
            return Response({"message": "신청이 승인되었습니다."}, status=status.HTTP_200_OK)
        else:
            applicant = application.applicant
            team = application.team
            notification_message = f"{team.name} 팀에서 팀 요청을 거절했어요"
            Notification.objects.create(user=applicant, message=notification_message, type="요청 결과")
            RejectedTeam.objects.create(user=applicant,team=team)
            application.delete()
            return Response({"message": "신청이 거절되었습니다."}, status=status.HTTP_200_OK)

# 알림
class NotificationListAPIView(APIView):
    def get(self, request):
        userPk = request.user.id
        user = get_object_or_404(User, pk=userPk)
        notifications = Notification.objects.filter(user=user).order_by('-created_at')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        userPk = request.user.id
        user = get_object_or_404(User, pk=userPk)
        notification_id = request.data.get("notification_id")

        notification = get_object_or_404(Notification, id=notification_id, user=user)
        notification.delete()
        return Response({"message": "알림이 삭제되었습니다."}, status=status.HTTP_200_OK)

# 스크랩 하기 (공모전 북마크하기)
class ScrapCreateAPIView(APIView):

    def post(self,request):
        contest_id = request.data.get("contest")
        user_id = 1 #request로 바꾸기
        user =User.objects.get(id=user_id) 

        try:
            scrap = Scrap.objects.get(user_id=user_id, contest_id=contest_id)
            scrap.delete() 
            return Response({'message': '스크랩 취소'}, status=status.HTTP_200_OK)
        except Scrap.DoesNotExist:
            contest = get_object_or_404(Contest, pk=contest_id)
            scrap = Scrap.objects.create(user_id=user_id, contest=contest)

            scrap_data = {
            "user": user.username,
            "contest": contest.title
            }
            return Response({'message': scrap_data}, status=status.HTTP_201_CREATED)
        
#스크랩목록보기
class ScrapAPIView(APIView):
    def get(self, request):
        user = request.user
        scraps = Scrap.objects.filter(user=user).select_related('contest')  # Scrap 객체에 연결된 Contest 객체 함께 로드

        response_data = []
        for scrap in scraps:
            scrap_data = ScrapSerializer(scrap).data
            contest_data = ContestSerializer(scrap.contest).data
            contest_data['is_scrapped'] = True
            scrap_data['contest'] = contest_data
            response_data.append(scrap_data)

        total_scraps = len(scraps)  # 스크랩한 대회의 수 계산

        response = {
            'total_scraps': total_scraps,
            'scrap_list': response_data
        }

        return Response(response, status=status.HTTP_200_OK)

# 찜하기 (팀 찜하기)
class JjimCreateAPIView(APIView):
    def post(self,request):
        team_id = request.data.get("team")
        user_id = 1 #request로 바꾸기
        user = User.objects.get(id=user_id)

        try:
            jjim = Jjim.objects.get(user_id=user_id, team_id=team_id)
            print(jjim.user)
            jjim.delete() 
            return Response({'message': '찜 취소'}, status=status.HTTP_200_OK)
        except Jjim.DoesNotExist:
            team = get_object_or_404(Team, pk=team_id)
            jjim = Jjim.objects.create(user_id=user_id, team=team)
            print(jjim.user)

            jjim_data = {
            "user": user.username,
            "team": team.teamname
            }
            return Response({'message': jjim_data}, status=status.HTTP_201_CREATED)

#찜 목록보기
class JjimAPIView(APIView):
    def get(self, request):
        user = request.user
        jjims = Jjim.objects.filter(user=user).select_related('team')  # Jjim 객체에 연결된 Team 객체 함께 로드

        response_data = []
        for jjim in jjims:
            jjim_data = JjimSerializer(jjim).data
            team_data = TeamSerializer(jjim.team).data
            contest_title = jjim.team.contest.title
            jjim_data['team'] = team_data
            team_data['contest_title'] = contest_title

            jjim_exists = Jjim.objects.filter(user=user, team=jjim.team).exists()
            team_data['is_jjim'] = jjim_exists

            for dev_member in team_data['dev_members']:
                if dev_member['user'] == team_data['created_by']:
                    dev_member['crown'] = True
                else:
                    dev_member['crown'] = False

            for plan_member in team_data['plan_members']:
                if plan_member['user'] == team_data['created_by']:
                    plan_member['crown'] = True
                else:
                    plan_member['crown'] = False

            for design_member in team_data['design_members']:
                if design_member['user'] == team_data['created_by']:
                    design_member['crown'] = True
                else:
                    design_member['crown'] = False

            response_data.append(jjim_data)

        total_teams = len(jjims)

        response = {
            'total_teams': total_teams,
            'jjim_list': response_data
        }

        return Response(response, status=status.HTTP_200_OK)

#[[[[[유저 정보받기 필요?]]]]]
class UserInfoAPIView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id

        serializer = UserInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#팀 생성페이지에서 생성자정보 보여주기
class TeamCreatePageAPIView(APIView):
    def get(self, request):
        user = request.user
        try:
            profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            return Response({"error": "UserProfile not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializer(profile)  # 시리얼라이저를 사용하여 데이터를 직렬화합니다

        return Response(serializer.data)