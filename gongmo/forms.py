from django import forms
from .models import *

class TeamForm(forms.ModelForm):
    dev_capacity = forms.IntegerField(min_value=0, initial=0)
    plan_capacity = forms.IntegerField(min_value=0, initial=0)
    design_capacity = forms.IntegerField(min_value=0, initial=0)
    class Meta:
        model = Team
        fields = ["name","teamname","call","detail","dev_capacity", "plan_capacity", "design_capacity"]
        labels = {
            "name":"제목",
            "teamname":"팀명",         
            "call":"연락 수단",
            "detail":"팀 소개 글",
            "dev_capacity": "개발 직군 정원",
            "plan_capacity": "기획 직군 정원",
            "design_capacity": "디자인 직군 정원"
        }

        def save(self, commit=True):
            team = super().save(commit=False)
            dev_capacity = self.cleaned_data["dev_capacity"]
            plan_capacity = self.cleaned_data["plan_capacity"]
            design_capacity = self.cleaned_data["design_capacity"]

            # Jickgoon 모델에서 해당하는 직군들을 가져옵니다.
            dev_jickgoon = Jickgoon.objects.get(name="dev")
            plan_jickgoon = Jickgoon.objects.get(name="plan")
            design_jickgoon = Jickgoon.objects.get(name="design")

            # Team 모델의 jickgoons 필드에 해당하는 Jickgoon 객체들을 추가합니다.
            team.jickgoons.add(dev_jickgoon, plan_jickgoon, design_jickgoon)

            # Team 모델의 필드에 dev_capacity, plan_capacity, design_capacity 값을 저장합니다.
            team.dev = dev_capacity
            team.plan = plan_capacity
            team.design = design_capacity

            if commit:
                team.save()

            return team