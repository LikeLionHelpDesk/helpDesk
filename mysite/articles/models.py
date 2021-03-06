from itertools import count
from select import select
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings


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
    tags = models.CharField(max_length = 255, null=True, blank=True) 

    def __str__(self):
        return self.subject

    def delete(self, *args, **kargs):
        if self.imgfile:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.imgfile.path))
        super(Question, self).delete(*args, **kargs)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    select = models.BooleanField(default=False)
    image = models.ImageField(upload_to ="articles/answer/", blank=True, null=True)

    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(Answer, self).delete(*args, **kargs)

