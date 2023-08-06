from django import forms
from .models import *

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ["name","teamname","call","detail"]
        labels = {
            "name":"제목",
            "teamname":"팀명",         
            "call":"연락 수단",
            "detail":"팀 소개 글"
        }
        
class JickgoonForm(forms.ModelForm):
    dev_capacity = forms.IntegerField(min_value=0, initial=0, label="개발 직군 정원")
    plan_capacity = forms.IntegerField(min_value=0, initial=0, label="기획 직군 정원")
    design_capacity = forms.IntegerField(min_value=0, initial=0, label="디자인 직군 정원")

    class Meta:
        model = Jickgoon
        fields = ['dev_capacity', 'plan_capacity', 'design_capacity']