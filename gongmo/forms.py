from django import forms
from .models import *

class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ["title"]

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ["name","teamname","call","detail"]
        # 다시추가해
        labels = {
            "name":"제목",
            "teamname": "팀명",
            "call": "연락 수단",
            "detail": "팀 소개 글",
        }

class JickgoonForm(forms.ModelForm):
    class Meta:
        model = Jickgoon
        fields = ['name']