import os
from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
from importlib_metadata import requires
from django.conf import settings

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    imgfile = models.ImageField(upload_to="articles/question/", blank=True, null=True)

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
    content = models.TextField(blank=True)
    create_date = models.DateTimeField()
    image = models.ImageField(upload_to ="articles/answer/", blank=True, null=True)

    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(Answer, self).delete(*args, **kargs)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
