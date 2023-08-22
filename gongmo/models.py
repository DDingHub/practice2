from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import json

class Contest(models.Model):
    title = models.CharField(max_length=255)
    photo = models.TextField()
    field = models.CharField(max_length=255)
    eligibility = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    sponsorship = models.CharField(max_length=255)
    application_period = models.CharField(max_length=255)
    prize_total = models.CharField(max_length=255)
    prize_first = models.CharField(max_length=255)
    website = models.URLField()
    details = models.TextField()
    isSchool = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True, null=True)
    viewCount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=50)
    teamname = models.CharField(max_length=100,null=True)
    call = models.CharField(max_length=100,null=True)
    detail = models.TextField(null=True)
    tendency = models.TextField(default="[]", null= True)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dev_capacity = models.PositiveIntegerField(default=0)
    plan_capacity = models.PositiveIntegerField(default=0)
    design_capacity = models.PositiveIntegerField(default=0)
    dev = models.PositiveIntegerField(default=0)
    plan = models.PositiveIntegerField(default=0)
    design = models.PositiveIntegerField(default=0)
    jickgoon_type = models.CharField(max_length=50, blank=True, choices=[('dev', '개발'), ('plan', '기획'), ('design', '디자인')])
    
    def get_tendency_as_list(self):
        return json.loads(self.tendency)

class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name = "members")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jickgoon = models.CharField(max_length=50, choices=[('dev', '개발'), ('plan', '기획'), ('design', '디자인')])

class Application(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    jickgoon = models.CharField(max_length=50, choices=[('dev', '개발'), ('plan', '기획'), ('design', '디자인')])
    is_approved = models.BooleanField(default=False)

class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta: unique_together = ['user','contest']

class Jjim(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta: unique_together = ['user','team']

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    message = models.TextField(null=True)
    is_read = models.BooleanField(default=False)

class UserInfo(models.Model):
    JICKGOON_CHOICES = [
        ('개발', '개발'),
        ('기획', '기획'),
        ('디자인', '디자인'),
    ]

    # HOBBY_CHOICES = [
    #     ('패션', '패션'),
    #     ('게임', '게임'),
    #     ('영화', '영화'),
    #     ('요리', '요리'),
    #     ('여행', '여행'),
    #     ('시사', '시사'),
    #     ('동물', '동물'),
    #     ('개그', '개그'),
    #     ('음악', '음악'),
    #     ('독서', '독서'),
    #     ('IT/기술', 'IT/기술'),
    #     ('개발', '개발')
    # ]

    # COURSE_CHOICES = [
    #     ('콘텐츠 기획', '콘텐츠 기획'),
    #     ('서비스 기획', '서비스 기획'),
    #     ('UX 디자인', 'UX 디자인'),
    #     ('UI 디자인', 'UI 디자인'),
    #     ('퍼포먼스 마케팅', '퍼포먼스 마케팅'),
    #     ('브랜드 기획', '브랜드 기획'),
    #     ('시스템 기획', '시스템 기획'),
    #     ('소싱', '소싱'),
    #     ('밸런스 디자인', '밸런스 디자인'),
    #     ('그래픽 디자인', '그래픽 디자인'),
    #     ('개발 전체', '개발 전체'),
    #     ('DBA', 'DBA'),
    #     ('IOS 개발', 'IOS 개발'),
    #     ('백엔드 개발', '백엔드 개발'),
    #     ('웹 개발', '웹 개발'),
    #     ('클라우드 개발', '클라우드 개발'),
    #     ('게임 개발', '게임 개발'),
    #     ('소프트웨어 개발', '소프트웨어 개발'),
    #     ('안드로이드 개발', '안드로이드 개발'),
    #     ('QA', 'QA'),
    #     ('네트워크/보안/운영', '네트워크/보안/운영'),
    #     ('프론트엔드 개발', '프론트엔드 개발'),
    #     ('데이터 분석가', '데이터 분석가'),
    #     ('데이터 엔지니어', '데이터 엔지니어'),
    #     ('빅데이터 사이언티스트', '빅데이터 사이언티스트'),
    #     ('머신러닝 엔지니어', '머신러닝 엔지니어')
    # ]

    # WORKING_TIME_CHOICES = [
    #     ('아침', '아침'),
    #     ('점심', '점심'),
    #     ('저녁', '저녁'),
    #     ('밤', '밤'),
    #     ('새벽', '새벽')
    # ]

    # CHARACTER_CHOICES = [
    #     ('솔직하다', '솔직하다'),
    #     ('활발하다', '활발하다'),
    #     ('논리적이다', '논리적이다'),
    #     ('성실하다', '성실하다'),
    #     ('리더쉽이 있다', '리더쉽이 있다'),
    #     ('도전적이다', '도전적이다'),
    #     ('성질이 급하다', '성질이 급하다'),
    #     ('꼼꼼하다', '꼼꼼하다'),
    #     ('배려심이 있다', '배려심이 있다'),
    #     ('과묵하다', '과묵하다'),
    #     ('센스있다', '센스있다'),
    #     ('협조적이다', '협조적이다'),
    #     ('통찰력이 높다', '통찰력이 높다'),
    #     ('열정적이다', '열정적이다'),
    #     ('의지력이 있다', '의지력이 있다'),
    #     ('느긋하다', '느긋하다')
    # ]

    # MBTI_CHOICES = [
    #     ('E', 'E'),
    #     ('I', 'I'),
    #     ('N', 'N'),
    #     ('S', 'S'),
    #     ('T', 'T'),
    #     ('F', 'F'),
    #     ('P', 'P'),
    #     ('J', 'J')
    # ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jickgoon_type = models.CharField(max_length=50, choices=JICKGOON_CHOICES)
    hobbies = models.JSONField(default=list)  
    courses = models.JSONField(default=list) 
    workingTimes = models.JSONField(default=list)  
    characters = models.JSONField(default=list)  
    mbti = models.JSONField(default=list)


