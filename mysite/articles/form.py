from cProfile import label
from dataclasses import fields
from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
<<<<<<< HEAD
        fields = ['subject', 'content', 'imgfile', 'tags']
=======
        fields = ['subject', 'content', 'imgfile']
>>>>>>> 14ae95d... first commit
        labels = {
            'subject' : '제목',
            'content' : '내용',
            'imgfile' : '파일',
<<<<<<< HEAD
            'tags' : '태그',
=======
>>>>>>> 14ae95d... first commit
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '내용'
        }