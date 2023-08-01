from django.shortcuts import render, redirect, get_object_or_404
import re
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.html import escape
from django.utils import timezone
from django.http import HttpResponseForbidden
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

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
def contest_list(request):
    save_contest_data()  # 크롤링 데이터 저장
    contests = Contest.objects.all()
    return render(request, 'contest_list.html', {'contests': contests})

class ContestListAPIView(APIView):
    def get(self, request):
        # 크롤링 함수 실행 (주기적으로 크롤링하여 데이터 저장)
        save_contest_data()
        contests = Contest.objects.all()
        serializer = ContestSerializer(contests, many=True)
        return Response(serializer.data)

#공모전 세부사항 보여주기
def contestDetail(request, contestPk):
    contest = get_object_or_404(Contest, pk=contestPk)
    teams = Team.objects.filter(contest=contest)
    context = {"contest": contest, "teams":teams}
    return render(request, "ddingapp/contestDetail.html", context)

class ContestDetailAPIView(APIView):
    def get(self, request, contestPk):
        contest = get_object_or_404(Contest, pk=contestPk)
        teams = Team.objects.filter(contest=contest)
        contest_serializer = ContestSerializer(contest)
        team_serializer = TeamSerializer(teams, many=True)
        return Response({'contest': contest_serializer.data, 'teams': team_serializer.data})

    def post(self, request, contestPk):
        # contest = get_object_or_404(Contest, pk=contestPk)
        # teamForm = TeamForm(request.POST)
        contest = get_object_or_404(Contest, pk=contestPk)
        data = JSONParser().parse(request)
        teamForm = TeamForm(data)
        teamForm.instance.contest = contest
        if teamForm.is_valid():
            teamPost = teamForm.save(commit=False)
            # teamPost.contest = request.contest
            # teamPost.created_by = request.user
            teamPost.save()
            teamForm.save_m2m()
            return Response({'message': '팀이 생성되었습니다.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': teamForm.errors}, status=status.HTTP_400_BAD_REQUEST)

#팀 세부사항 보여주기
@login_required
def teamDetail(request, contestPk, teamPk):
    team = get_object_or_404(Team, pk=teamPk)
    jickgoons = team.jickgoons.all()
    member = team.member_set.filter(user=request.user).first()
    if member:
        member_jickgoon = member.jickgoon.name
    else:
        member_jickgoon = None

    is_team_creator = team.created_by == request.user

    context = {
        'team': team,
        'jickgoons': jickgoons,
        'member_jickgoon': member_jickgoon,
        'dev_capacity': team.get_dev_capacity(),
        'plan_capacity': team.get_plan_capacity(),
        'design_capacity': team.get_design_capacity(),
        'is_team_creator': is_team_creator,
    }
    return render(request, 'ddingapp/teamDetail.html', context)

#팀 참가, 신청하기
@login_required
def teamJoin(request, contestPk, teamPk):
    team = get_object_or_404(Team, pk=teamPk)
    jickgoons = Jickgoon.objects.filter(name__in=['기획', '개발', '디자인'])

    if request.method == 'POST':
        selected_jickgoons_ids = request.POST.getlist('jickgoons')
        team.member_set.filter(user=request.user).delete()
        
        is_team_creator = team.created_by == request.user

        dev_capacity = team.dev_capacity
        plan_capacity = team.plan_capacity
        design_capacity = team.design_capacity

        member_counts = {
            '개발': team.member_set.filter(jickgoon__name='개발').count(),
            '기획': team.member_set.filter(jickgoon__name='기획').count(),
            '디자인': team.member_set.filter(jickgoon__name='디자인').count(),
        }       

        if is_team_creator:  # 팀 제작자인 경우 바로 가입
            for jickgoon_id in selected_jickgoons_ids:
                jickgoon = get_object_or_404(Jickgoon, id=jickgoon_id)
                Member.objects.create(user=request.user, team=team, jickgoon=jickgoon)
                member_counts[jickgoon.name] += 1

            return redirect('teamDetail', contestPk=contestPk, teamPk=teamPk)
        else:  # 팀 제작자가 아닌 경우 알림 생성 후 대기
            for jickgoon_id in selected_jickgoons_ids:
                jickgoon = get_object_or_404(Jickgoon, id=jickgoon_id)
                if (jickgoon.name == '개발' and member_counts['개발'] >= dev_capacity) or \
                   (jickgoon.name == '기획' and member_counts['기획'] >= plan_capacity) or \
                   (jickgoon.name == '디자인' and member_counts['디자인'] >= design_capacity):
                    messages.error(request, f"{jickgoon.name} 직군의 참가 인원 수가 이미 초과되었습니다.")
                    return redirect('teamDetail', contestPk=contestPk, teamPk=teamPk)
                
                notification_message = f"{escape(request.user.username)} 님이 {escape(team.name)} 팀에 {escape(jickgoon.name)} 직군으로 참여 신청하였습니다. ({timezone.now().strftime('%Y-%m-%d %H:%M')})"
                notification = Notification.objects.create(user=request.user, team=team, jickgoon=jickgoon, message=notification_message)

            messages.success(request, "팀 제작자의 승인이 필요한 팀 신청이 완료되었습니다. 승인 후 팀에 가입됩니다.")
            return redirect('teamDetail', contestPk=contestPk, teamPk=teamPk)
    
    context = {
        'team': team,
        'jickgoons': jickgoons,
    }
    return render(request, 'ddingapp/teamJoin.html', context)

#마이페이지, 알림, 팀 수락 거절
@login_required
def mypage(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    teams = Team.objects.filter(member__user=user)
    teamsteams = Team.objects.filter(created_by=user)
    notifications = Notification.objects.filter(team__created_by=user)
    context = {
        'user': user,
        'teams':teams,
        'teamsteams': teamsteams,
        'notifications': notifications,
        }
    return render(request, 'ddingapp/mypage.html', context)

#팀원 내보내기
@login_required
def removeMember(request, teamPk):
    team = get_object_or_404(Team, pk=teamPk)

    if request.method == 'POST':
        member_pk = request.POST.get('memberPk')
        member = get_object_or_404(Member, pk=member_pk)

        if request.user == team.created_by and request.user != member.user:
            member.delete()
            messages.success(request, f"{member.user.username} 님을 팀에서 퇴출시켰습니다.")
        else:
            messages.error(request, "팀 제작자만 팀원을 퇴출시킬 수 있습니다.")

    return redirect('teamDetail', contestPk=team.contest.pk, teamPk=teamPk)

#팀원 수락
@login_required
def approveJoinRequest(request, notification_pk):
    notification = get_object_or_404(Notification, pk=notification_pk)

    # 팀 제작자인지 확인
    if request.user != notification.team.created_by:
        return HttpResponseForbidden()

    # 알림 삭제
    notification.delete()

    # 해당 사용자를 팀에 추가
    Member.objects.create(user=notification.user, team=notification.team, jickgoon=notification.jickgoon)

    messages.success(request, f"{notification.user.username} 님의 팀 참가 신청을 승인하였습니다.")
    return redirect('teamDetail', contestPk=notification.team.contest.pk, teamPk=notification.team.pk)

#팀원 거절
def rejectJoinRequest(request, notification_pk):
    notification = get_object_or_404(Notification, pk=notification_pk)
    
    if notification.team.created_by == request.user:
        notification.delete()
    else:
        return HttpResponseForbidden()
    
    return redirect(reverse('mypage', args=[request.user.id]))