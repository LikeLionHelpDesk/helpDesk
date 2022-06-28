<<<<<<< HEAD
from itertools import count
from re import A
from django.shortcuts import render
from articles.models import Question
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    test = Question.objects.filter(subject__icontains = '\"')[:6]
    if request.method == 'POST' and 'category' in request.POST:
        category_name = request.POST['category']
        if category_name:
            test = Question.objects.filter(Q(subject__icontains = category_name) | Q(tags__icontains = category_name))[:6]
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date') # 작성일시 역순으로 정렬
    new_question = Question.objects.order_by('-count')[:6]

    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'new_question' : new_question, 'test' : test} # {'question_list': <QuerySet [<Question: 장고 모델 질문입니다.>, <Question: pybo가 무엇인가요?>]>}
=======
from django.shortcuts import render
from articles.models import Question
from django.core.paginator import Paginator

def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date') # 작성일시 역순으로 정렬
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj} # {'question_list': <QuerySet [<Question: 장고 모델 질문입니다.>, <Question: pybo가 무엇인가요?>]>}
>>>>>>> 14ae95d... first commit
    return render(request, 'index.html', context)

