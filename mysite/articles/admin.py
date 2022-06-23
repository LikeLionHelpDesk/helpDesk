from django.contrib import admin
from .models import Question, Answer

admin.site.register(Question)
admin.site.register(Answer) 
#admin 에서 db 확인
# Register your models here.
