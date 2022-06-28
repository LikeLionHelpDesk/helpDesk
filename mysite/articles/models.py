<<<<<<< HEAD
import os
from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
from importlib_metadata import requires
from django.conf import settings
=======
from django.db import models
from django.contrib.auth.models import User
>>>>>>> 14ae95d... first commit

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
<<<<<<< HEAD
    imgfile = models.ImageField(upload_to="articles/question/", blank=True, null=True)
    count = models.PositiveIntegerField(default=0)
    solved = models.BooleanField(default=False)
    selected_question = models.PositiveIntegerField(default=0)
    tags = models.CharField(max_length = 255, null=True, blank=True) 
=======
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
>>>>>>> 14ae95d... first commit

    def __str__(self):
        return self.subject

<<<<<<< HEAD
    def delete(self, *args, **kargs):
        if self.imgfile:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.imgfile.path))
        super(Question, self).delete(*args, **kargs)

=======
>>>>>>> 14ae95d... first commit
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)
<<<<<<< HEAD
    content = models.TextField(blank=True)
    create_date = models.DateTimeField()
    image = models.ImageField(upload_to ="articles/answer/", blank=True, null=True)
    select = models.BooleanField(default=False)
    
    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(Answer, self).delete(*args, **kargs)
=======
    content = models.TextField()
    create_date = models.DateTimeField()

>>>>>>> 14ae95d... first commit
