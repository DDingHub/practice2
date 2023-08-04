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
        data = request.data
        if request.user.is_authenticated:
            teamForm = TeamForm(data)
            teamForm.instance.contest = contest
            if teamForm.is_valid():
                teamPost = teamForm.save(commit=False)
                teamPost.created_by = request.user
                teamPost.dev_capacity = teamForm.cleaned_data['dev_capacity']
                teamPost.plan_capacity = teamForm.cleaned_data['plan_capacity']
                teamPost.design_capacity = teamForm.cleaned_data['design_capacity']
                teamPost.save()
                teamForm.save_m2m()
                return Response({'message': '팀이 생성되었습니다.'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': teamForm.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': '로그인한 사용자만 팀을 생성할 수 있습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

#팀 세부페이지
class TeamDetailAPIView(APIView):
    #팀 세부페이지 가져오기
    def get(self, request, contestPk, teamPk):
        team = get_object_or_404(Team, pk=teamPk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    #팀 지원하기
    def post(self, request, contestPk, teamPk):
        team = get_object_or_404(Team, pk=teamPk)
        data = request.data
        serializer = TeamSerializer(data=data)

        if serializer.is_valid():
            selected_jickgoons_ids = serializer.validated_data.get('jickgoons')
            team.member_set.filter(user=request.user).delete()
        
            is_team_creator = team.created_by == request.user

            dev_capacity = team.dev
            plan_capacity = team.plan
            design_capacity = team.design

            member_counts = {
                '개발': team.member_set.filter(jickgoon__name='개발').count(),
                '기획': team.member_set.filter(jickgoon__name='기획').count(),
                '디자인': team.member_set.filter(jickgoon__name='디자인').count(),
            }       

            if is_team_creator:
                for jickgoon_id in selected_jickgoons_ids:
                    if jickgoon_id == 1:  # 개발 직군 ID
                        team.dev += 1
                    elif jickgoon_id == 2:  # 기획 직군 ID
                        team.plan += 1
                    elif jickgoon_id == 3:  # 디자인 직군 ID
                        team.design += 1
                    team.save()

                return Response({'message': '팀에 가입되었습니다.'}, status=status.HTTP_201_CREATED)
            else:
                for jickgoon_id in selected_jickgoons_ids:
                    if (jickgoon_id == 1 and member_counts['개발'] >= dev_capacity) or \
                       (jickgoon_id == 2 and member_counts['기획'] >= plan_capacity) or \
                       (jickgoon_id == 3 and member_counts['디자인'] >= design_capacity):
                        return Response({'error': f"해당 직군의 참가 인원 수가 이미 초과되었습니다."}, status=status.HTTP_400_BAD_REQUEST)
                
                    notification_message = f"{escape(request.user.username)} 님이 {escape(team.name)} 팀에 참여 신청하였습니다. ({timezone.now().strftime('%Y-%m-%d %H:%M')})"
                    notification = Notification.objects.create(user=request.user, team=team, jickgoon_id=jickgoon_id, message=notification_message)

                return Response({'message': '팀 가입 요청이 완료되었습니다. 팀 제작자의 승인을 기다려주세요.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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