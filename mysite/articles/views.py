<<<<<<< HEAD
from account.models import Profile
=======
from multiprocessing import context
from unicodedata import name
>>>>>>> 14ae95d... first commit
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.http import HttpResponseNotAllowed
from django.utils import timezone
from .form import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='../users/login')
def new(request):
    if request.method == 'POST': # post 가 아닌 POST 로 작성
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
<<<<<<< HEAD
            question.imgfile = request.FILES.get('imgfile')
            question.create_date = timezone.now()
            question.author = request.user
            question.save()
        return redirect('index')
    else:
        form = QuestionForm()
        
=======
            question.imgfile = request.FILES['imgfile']
            print(question.imgfile)
            question.create_date = timezone.now()
            question.author = request.user
            question.save()
            return redirect('index')
    else:
        form = QuestionForm()
>>>>>>> 14ae95d... first commit
    context = {'form' : form}
    return render(request, 'new.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {'question' : question}
    return render(request, 'detail.html', context)

@login_required(login_url='../../../users/login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
<<<<<<< HEAD
        if form.is_valid():
=======
        if form.is_valid:
>>>>>>> 14ae95d... first commit
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.author = request.user
<<<<<<< HEAD
            answer.image = request.FILES.get('image')
=======
>>>>>>> 14ae95d... first commit
            answer.save()
            return redirect('detail', question_id = question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'detail', context)

@login_required(login_url='../login')
def edit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('detail', question_id=question.id)
    if request.method == "POST":
        print('a')
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('detail', question_id=question.id)
    else: 
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'new.html', context)

def delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
<<<<<<< HEAD
    # answer = get_object_or_404(Answer, pk=question_id)
=======
>>>>>>> 14ae95d... first commit
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
<<<<<<< HEAD
    # answer.delete()
    return redirect('index')

def test(request):
    return render(request, 'test.html')

@login_required(login_url='../../../users/login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다!')
    else:
        answer.delete()
    return redirect('detail', question_id=answer.question.id)

@login_required(login_url='../../../users/login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('detail', question_id=answer.question.id)
    
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('detail', question_id=answer.question.id)
        else:
            form = AnswerForm(instance=answer)
        context = {'answer' : answer, 'form' : form}
        return render(request, 'detail.html', context)

def select(request, question_id, answer_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = get_object_or_404(Answer, pk = answer_id)
    profile = get_object_or_404(Profile, nickname = answer.author.profile.nickname)
    if('select' in request.POST):
        answer.select = True
        if(question.solved == False):
            question.solved = True
        profile.adopted_answer += 1
        question.selected_question += 1
        answer.save()
        question.save()
        profile.save()
    elif('cancel' in request.POST):
        answer.select = False
        if(profile.adopted_answer != 0):
            profile.adopted_answer -= 1
        question.selected_question -= 1        
        if(question.selected_question == 0 and question.solved == True):
            question.solved = False
        profile.save()
        answer.save()
        question.save()
    return redirect('detail', question_id=question.id)
=======
    return redirect('index')

def test(request):
    return render(request, 'test.html')
>>>>>>> 14ae95d... first commit
