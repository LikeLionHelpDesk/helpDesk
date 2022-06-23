from itertools import count
from select import select
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    count = models.PositiveIntegerField(default=0)
    solved = models.BooleanField(default=False)
    selected_question = models.PositiveIntegerField(default=0)
    # tag = models.CharField(max_length = 255) 

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    select = models.BooleanField(default=False)

