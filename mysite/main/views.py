from itertools import count
from re import A
from django.shortcuts import get_list_or_404, render, get_object_or_404
from articles.models import Question
from django.core.paginator import Paginator

def index(request):
    if request.method == 'POST':
        category_name = request.POST['category']
        tmp = Question.objects.all()
        if category_name:
            test = tmp.filter(subject=category_name)
        print(test)
    else:
        test = Question.objects.all()
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date') # 작성일시 역순으로 정렬
    new_question = Question.objects.order_by('-count')[:6]

    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'new_question' : new_question, } # {'question_list': <QuerySet [<Question: 장고 모델 질문입니다.>, <Question: pybo가 무엇인가요?>]>}
    return render(request, 'index.html', context)
