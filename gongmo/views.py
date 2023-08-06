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
    def get(self, request, teamPk, contestPk):
        team = get_object_or_404(Team, pk=teamPk)
        members = Member.objects.filter(team=team)

        dev_members = members.filter(jickgoon='dev')
        plan_members = members.filter(jickgoon='plan')
        design_members = members.filter(jickgoon='design')

        dev_member_data = [{'user': member.user.username, 'jickgoon': member.jickgoon} for member in dev_members]
        plan_member_data = [{'user': member.user.username, 'jickgoon': member.jickgoon} for member in plan_members]
        design_member_data = [{'user': member.user.username, 'jickgoon': member.jickgoon} for member in design_members]

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

        if jickgoon_type == "dev" and team.dev < team.dev_capacity:
            team.dev += 1
        elif jickgoon_type == "plan" and team.plan < team.plan_capacity:
            team.plan += 1
        elif jickgoon_type == "design" and team.design < team.design_capacity:
            team.design += 1
        else:
            return Response({"error": "The selected jickgoon capacity is already full for this team."},
                        status=status.HTTP_400_BAD_REQUEST)

        Member.objects.create(team=team, user=request.user, jickgoon=jickgoon_type)
        team.save()

        return Response({"message": "You have successfully applied to the team."},
                    status=status.HTTP_201_CREATED)


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


class MyTeamAPIView(APIView):
    def get(self, reqeust, userPk):
        teams_created = Team.objects.filter(created_by=userPk)
        teams_joined = Team.objects.filter(members__user=userPk)
        teams_created_data = [{'team_id': team.id} for team in teams_created]
        teams_joined_data = [{'team_id': team.id} for team in teams_joined]

        return Response({"my_teams_created": teams_created_data, "my_teams_joined": teams_joined_data}, status=status.HTTP_200_OK)

class TeamManagementAPIView(APIView):
    def get(self, request, userPk):
        teams_created = Team.objects.filter(created_by=userPk)

        team_data = []
        for team in teams_created:
            dev_members = team.members.filter(jickgoon='dev')
            plan_members = team.members.filter(jickgoon='plan')
            design_members = team.members.filter(jickgoon='design')

            dev_member_data = [{'user': member.user.username, 'jickgoon': member.jickgoon} for member in dev_members]
            plan_member_data = [{'user': member.user.username, 'jickgoon': member.jickgoon} for member in plan_members]
            design_member_data = [{'user': member.user.username, 'jickgoon': member.jickgoon} for member in design_members]

            team_data.append({
                'id': team.id,
                'dev_members': dev_member_data,
                'plan_members': plan_member_data,
                'design_members': design_member_data,
            })

        return Response(team_data, status=status.HTTP_200_OK)

    def post(self, request, userPk):
        user = get_object_or_404(User, pk=userPk)

        # Get the request data
        team_id = request.data.get("team_id")
        membername = request.data.get("membername")
        jickgoon_type = request.data.get("jickgoon_type")

        try:
            # Get the team object
            team = Team.objects.get(pk=team_id)

            # Check if the user is the creator of the team
            if team.created_by == user:
                # Find the member with the given membername and jickgoon_type in the team
                try:
                    member = Member.objects.get(team=team, user__username=membername, jickgoon=jickgoon_type)
                except Member.DoesNotExist:
                    return Response({"error": "The specified member with the given jickgoon_type was not found in the team."},
                                    status=status.HTTP_404_NOT_FOUND)

                # Update the team capacity
                if jickgoon_type == "dev":
                    team.dev -= 1
                elif jickgoon_type == "plan":
                    team.plan -= 1
                elif jickgoon_type == "design":
                    team.design -= 1

                # Save the updated team
                team.save()

                # Remove the member from the team
                member.delete()

                return Response({"message": "The member has been removed from the team successfully."},
                                status=status.HTTP_200_OK)
            else:
                return Response({"error": "You are not authorized to remove a member from this team."},
                                status=status.HTTP_401_UNAUTHORIZED)
        except Team.DoesNotExist:
            return Response({"error": "The specified team does not exist."},
                            status=status.HTTP_404_NOT_FOUND)


    
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