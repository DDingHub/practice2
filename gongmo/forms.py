from django import forms
from .models import *

class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ["title"]

class TeamForm(forms.ModelForm):
    plan_capacity = forms.IntegerField(min_value=0, initial=0)
    dev_capacity = forms.IntegerField(min_value=0, initial=0)
    design_capacity = forms.IntegerField(min_value=0, initial=0)

    class Meta:
        model = Team
        fields = ["name","teamname","call","detail", "plan_capacity", "dev_capacity", "design_capacity"]
        labels = {
            "name":"제목",
            "teamname": "팀명",
            "call": "연락 수단",
            "detail": "팀 소개 글",
            "dev_capacity": "개발 인원 수",
            "plan_capacity": "기획 인원 수",
            "design_capacity": "디자인 인원 수",
        }

class JickgoonForm(forms.ModelForm):
    class Meta:
        model = Jickgoon
        fields = ['name']