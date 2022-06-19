from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def profile(request, user_id):
    client1 = get_object_or_404(User, pk=user_id)
    client_obj = Profile.objects.get(user=client1)
    context = {'profile' : client_obj}
    return render(request, 'profile.html', context)