from django import forms
from .models import *
from django.forms import formset_factory
import json

class TendencyForm(forms.Form):
    tendency = forms.CharField()

TendencyFormSet = formset_factory(TendencyForm, extra=1)


class TeamForm(forms.ModelForm):
    tendency = forms.JSONField(label="팀 성향", required=False)

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

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.tendency_formset = TendencyFormSet()

        def is_valid(self):
            return super().is_valid() and self.tendency_formset.is_valid()

        def save(self, commit=True):
            instance = super().save(commit=commit)
            if commit:
                instance.tendency = self.cleaned_data.get("tendency")
                instance.save()
            return instance
        
class DDingContestForm(forms.ModelForm):
    class Meta:
        model =Contest
        fields = '__all__'