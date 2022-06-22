from cProfile import label
from dataclasses import fields
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'school', 'git_address','bio']
        labels = {
            'nickname' : '닉네임',
            'school' : '학교', 
            'git_address' : '깃 주소',
            'bio' : '내 소개' 
        }

