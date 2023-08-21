from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
import re
import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.urls import reverse
from django.utils.html import escape
from django.utils import timezone
from django.http import HttpResponseForbidden
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist

url = "https://www.wevity.com/?c=find&s=1&gub=1&cidx=20&gp="

def save_contest_data():
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
                            details=dicttt.get('상세정보')
                        )
                        contest.save()

#공모전 목록 보여주기
class ContestListAPIView(APIView):
    def get(self, request):
        # save_contest_data()
        contests = Contest.objects.filter(isSchool=False)
        serializer = ContestSerializer(contests, many=True)
        return Response(serializer.data)

#교내 공모전 목록
class DDingContestListAPIView(APIView):
    def get(self, request):
        dding_contests = Contest.objects.filter(isSchool=True)
        serializer = ContestSerializer(dding_contests, many=True)
        return Response(serializer.data)

    def post(self,request):
        dding_contest_form = DDingContestForm(request.data)
        if dding_contest_form.is_valid():
            dding_contest_form.save()
            return Response(dding_contest_form.cleaned_data, status=status.HTTP_201_CREATED)
        return Response(dding_contest_form.errors, status=status.HTTP_400_BAD_REQUEST)


#공모전 세부페이지
class ContestDetailAPIView(APIView):
    #공모전 정보와 팀 정보 가져오기
    def get(self, request, contestPk):
        contest = get_object_or_404(Contest, pk=contestPk)
        teams = Team.objects.filter(contest=contest)
        contest_serializer = ContestSerializer(contest)
        team_serializer = TeamSerializer(teams, many=True)
        return Response({'contest': contest_serializer.data, 'teams': team_serializer.data})
    #팀 생성하기
    def post(self, request, contestPk):
        contest = get_object_or_404(Contest, pk=contestPk)
        team_form = TeamForm(request.data)

        if team_form.is_valid():
            team = team_form.save(commit=False)
            team.contest = contest
            team.created_by = request.user
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
        team = get_object_or_404(Team, pk=teamPk)
        members = Member.objects.filter(team=team)
        dev_members = members.filter(jickgoon='dev')
        plan_members = members.filter(jickgoon='plan')
        design_members = members.filter(jickgoon='design')

        dev_member_data = [{'user': member.user.username} for member in dev_members]
        plan_member_data = [{'user': member.user.username} for member in plan_members]
        design_member_data = [{'user': member.user.username} for member in design_members]

        team_serializer = TeamSerializer(team)
        data = {
            **team_serializer.data,
            'dev_members': dev_member_data,
            'plan_members': plan_member_data,
            'design_members': design_member_data,
        }

        return Response(data)

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
            Notification.objects.create(user=team.created_by, message=notification_message)

        return Response({"message": "팀 지원이 완료되었습니다. 팀장의 승인을 기다려주세요."},status=status.HTTP_201_CREATED)

# 회원가입
class SignUpAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': '사용자 이름과 비밀번호를 입력해주세요.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': '이미 존재하는 사용자 이름입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(username=username, password=make_password(password))
        user.save()
        return Response({'message': '회원가입이 완료되었습니다.'}, status=status.HTTP_201_CREATED)
# 로그인
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

        user_data = {
                "id": request.user.id,
                "username": request.user.username
            }
        
        response_data = {
                "message": "로그인 완료.",
                "user": user_data
            }
        
        return Response(response_data, status=status.HTTP_201_CREATED)
# 로그아웃
class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': '로그아웃이 완료되었습니다.'}, status=status.HTTP_200_OK)

#My팀 보기(지원한 팀, 만든 팀)
class MyTeamAPIView(APIView):
    def get(self, reqeust, userPk):
        teams_created = Team.objects.filter(created_by=userPk)
        teams_joined = Team.objects.filter(members__user=userPk)
        teams_created_data = [{'team_id': team.id} for team in teams_created]
        teams_joined_data = [{'team_id': team.id} for team in teams_joined]

        return Response({"my_teams_created": teams_created_data, "my_teams_joined": teams_joined_data}, status=status.HTTP_200_OK)

# 팀장 : 지원자, 팀원 관리
class TeamManagementAPIView(APIView):
    # 내 팀에 신청한 사람 가져오기
    def get(self, request, userPk):
        user = get_object_or_404(User, pk=userPk)
        teams_created_by_user = Team.objects.filter(created_by=user)

        # 나의 팀들에 대한 신청 정보 가져오기
        applications = Application.objects.filter(team__in=teams_created_by_user)
        application_data = []
        
        # 나의 팀들에 대한 멤버 정보 가져오기
        member_data = []

        for team in teams_created_by_user:
            members = Member.objects.filter(team=team)
            for member in members:
                member_data.append({
                    "team_id": team.id,
                    "user_id": member.user.id,
                    "jickgoon_type": member.jickgoon
                })
            
            applications_for_team = applications.filter(team=team)
            for application in applications_for_team:
                application_data.append({
                    "id": application.id,
                    "team": application.team.id,
                    "applicant": application.applicant.id,
                    "jickgoon": application.jickgoon,
                    "is_approved": application.is_approved
                })

        response_data = {
            "applications": application_data,
            "members": member_data
        }

        return Response(response_data, status=status.HTTP_200_OK)

    # 내 팀에 신청한 사람의 신청 승인 또는 거절
    def put(self, request, userPk):
        user = get_object_or_404(User, pk=userPk)
        application_id = request.data.get("application_id")
        is_approved = request.data.get("is_approved")

        application = get_object_or_404(Application, id=application_id, team__created_by=user)

        if is_approved == "true":
            application.is_approved = True
            application.save()
            applicant = application.applicant
            team = application.team
            notification_message = f"{team.name} 팀에서 팀 요청을 수락했어요!"
            Notification.objects.create(user=applicant, message=notification_message)

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
            Notification.objects.create(user=applicant, message=notification_message)
            application.delete()
            return Response({"message": "신청이 거절되었습니다."}, status=status.HTTP_200_OK)

    # 내 팀에 들어와 있는 사람 내보내기
    def post(self, request, userPk):
        user = get_object_or_404(User, pk=userPk)
        team_id = request.data.get("team_id")
        user_id = request.data.get("user_id")


        try:
            team = get_object_or_404(Team, id=team_id, created_by=user)
            member = get_object_or_404(Member, id=user_id, team=team)
            member.delete()
            return Response({"message": "멤버가 팀에서 내보내졌습니다."}, status=status.HTTP_200_OK)
        except Team.DoesNotExist:
            return Response({"error": "해당 팀을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        except Member.DoesNotExist:
            return Response({"error": "해당 멤버를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(team_id)
            request.data.get("user_id")
            return Response({"errorasdfaesf": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 알림 확인, 삭제
class NotificationListAPIView(APIView):
    def get(self, request, userPk):
        user = get_object_or_404(User, pk=userPk)
        notifications = Notification.objects.filter(user=user).order_by('-created_at')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    def post(self, request, userPk):
        user = get_object_or_404(User, pk=userPk)
        notification_id = request.data.get("notification_id")
        is_read = request.data.get("is_read")

        notification = get_object_or_404(Notification, id=notification_id, user=user)
        if is_read == "true":
            notification.is_read = True
            notification.delete()
            return Response({"message": "알림이 삭제되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)
        
# 스크랩 하기 (공모전 북마크하기)
class ScrapCreateAPIView(APIView):
    def post(self,request):
        contest_id = request.data.get("contest")
        user =request.user

        try:
            scrap = Scrap.objects.get(user=user, contest_id=contest_id)
            scrap.delete() 
            return Response({'message': '스크랩 취소'}, status=status.HTTP_200_OK)
        except Scrap.DoesNotExist:
            contest = get_object_or_404(Contest, pk=contest_id)
            scrap = Scrap.objects.create(user=user, contest=contest)

            scrap_data = {
            "user": user.username,
            "contest": contest.title
            }
            return Response({'message': scrap_data}, status=status.HTTP_201_CREATED)
        
#스크랩목록보기
class ScrapListAPIView(ListAPIView):
    serializer_class = ScrapSerializer

    def get_queryset(self):
        user_pk = self.kwargs["userPk"]
        return Scrap.objects.filter(user__pk=user_pk)


# 찜하기 (팀 찜하기)
class JjimCreateAPIView(APIView):
    def post(self,request):
        team_id = request.data.get("team")
        user =request.user

        try:
            jjim = Jjim.objects.get(user=user, team_id=team_id)
            jjim.delete() 
            return Response({'message': '찜 취소'}, status=status.HTTP_200_OK)
        except Jjim.DoesNotExist:
            team = get_object_or_404(Team, pk=team_id)
            jjim = Jjim.objects.create(user=user, team=team)

            jjim_data = {
            "user": user.username,
            "team": team.teamname
            }
            return Response({'message': jjim_data}, status=status.HTTP_201_CREATED)

#찜 목록보기
class JjimListAPIView(ListAPIView):
    serializer_class = JjimSerializer

    def get_queryset(self):
        user_pk = self.kwargs["userPk"]
        return Jjim.objects.filter(user__pk=user_pk)

#유저 정보받기
class UserInfoAPIView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id

        serializer = UserInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)