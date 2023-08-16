from django import forms
from .models import *

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ["name","teamname","call","detail", "dev_capacity", "plan_capacity", "design_capacity"]
        labels = {
            "name":"제목",
            "teamname":"팀명",         
            "call":"연락 수단",
            "detail":"팀 소개 글",
            "dev_capacity" : "개발",
            "plan_capacity" : "기획",
            "design_capacity" : "디자인"
        }
        
class DDingContestForm(forms.ModelForm):
    class Meta:
        model = DDingContest
        fields = '__all__'