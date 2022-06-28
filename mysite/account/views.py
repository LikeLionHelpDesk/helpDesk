import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
 
from articles.models import Question

from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from .forms import ProfileForm

# Create your views here.
def profile(request, user_id):
    question_list = Question.objects.order_by('-create_date') # 작성일시 역순으로 정렬
    client1 = get_object_or_404(User, pk=user_id)
    client_obj = Profile.objects.get(user=client1)
    image = request.FILES.get('image')
    context = {'profile' : client_obj, 'question_list' : question_list, 'image' : image,}
    return render(request, 'profile.html', context)

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        profile_form.image = request.FILES.get('image')
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'update_profile.html', {
        'profile_form': profile_form
    })
