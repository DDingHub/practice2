from django import forms
from .models import *

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'