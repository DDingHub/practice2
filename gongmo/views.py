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
        save_contest_data()
        contests = Contest.objects.all()
        serializer = ContestSerializer(contests, many=True)
        return Response(serializer.data)

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

            return Response({'message': '팀이 생성되었습니다.'}, status=status.HTTP_201_CREATED)
        else:
            errors = {}
            errors.update(team_form.errors)
            return Response({'error': errors}, status=status.HTTP_400_BAD_REQUEST)

#팀 세부페이지
class TeamDetailAPIView(APIView):
    #팀 세부페이지 가져오기
    def get(self, request, teamPk, contestPk,jickgoonPk):
        team = get_object_or_404(Team, pk=teamPk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    #팀 지원하기
    def post(self, request, teamPk, jickgoonPk, contestPk):
        team = get_object_or_404(Team, pk=teamPk)
        jickgoon = get_object_or_404(Jickgoon, pk=jickgoonPk)

        if team.dev <= jickgoon.dev_capacity and team.plan <= jickgoon.plan_capacity and team.design <= jickgoon.design_capacity:
            # Check if the team still has available slots for the selected jickgoon
            if team.dev < jickgoon.dev_capacity:
                team.dev += 1
            elif team.plan < jickgoon.plan_capacity:
                team.plan += 1
            elif team.design < jickgoon.design_capacity:
                team.design += 1
            else:
                return Response({"error": "The selected jickgoon capacity is already full for this team."},
                                status=status.HTTP_400_BAD_REQUEST)

            # Save the team object with the updated jickgoon capacity
            team.save()
            
            # Save the application information
            team.created_by = request.user
            team.jickgoons.add(jickgoon)
            team.save()
            
            return Response({"message": "You have successfully applied to the team."},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "The selected jickgoon capacity is not available for this team."},
                            status=status.HTTP_400_BAD_REQUEST)

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
        return Response({'message': '로그인이 완료되었습니다.'}, status=status.HTTP_200_OK)

# 로그아웃
class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': '로그아웃이 완료되었습니다.'}, status=status.HTTP_200_OK)


# #마이페이지, 알림, 팀 수락 거절
# @login_required
# def mypage(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     teams = Team.objects.filter(member__user=user)
#     teamsteams = Team.objects.filter(created_by=user)
#     notifications = Notification.objects.filter(team__created_by=user)
#     context = {
#         'user': user,
#         'teams':teams,
#         'teamsteams': teamsteams,
#         'notifications': notifications,
#         }
#     return render(request, 'ddingapp/mypage.html', context)

# #팀원 내보내기
# @login_required
# def removeMember(request, teamPk):
#     team = get_object_or_404(Team, pk=teamPk)

#     if request.method == 'POST':
#         member_pk = request.POST.get('memberPk')
#         member = get_object_or_404(Member, pk=member_pk)

#         if request.user == team.created_by and request.user != member.user:
#             member.delete()
#             messages.success(request, f"{member.user.username} 님을 팀에서 퇴출시켰습니다.")
#         else:
#             messages.error(request, "팀 제작자만 팀원을 퇴출시킬 수 있습니다.")

#     return redirect('teamDetail', contestPk=team.contest.pk, teamPk=teamPk)

# #팀원 수락
# @login_required
# def approveJoinRequest(request, notification_pk):
#     notification = get_object_or_404(Notification, pk=notification_pk)

#     # 팀 제작자인지 확인
#     if request.user != notification.team.created_by:
#         return HttpResponseForbidden()

#     # 알림 삭제
#     notification.delete()

#     # 해당 사용자를 팀에 추가
#     Member.objects.create(user=notification.user, team=notification.team, jickgoon=notification.jickgoon)

#     messages.success(request, f"{notification.user.username} 님의 팀 참가 신청을 승인하였습니다.")
#     return redirect('teamDetail', contestPk=notification.team.contest.pk, teamPk=notification.team.pk)

# #팀원 거절
# def rejectJoinRequest(request, notification_pk):
#     notification = get_object_or_404(Notification, pk=notification_pk)
    
#     if notification.team.created_by == request.user:
#         notification.delete()
#     else:
#         return HttpResponseForbidden()
    
#     return redirect(reverse('mypage', args=[request.user.id]))