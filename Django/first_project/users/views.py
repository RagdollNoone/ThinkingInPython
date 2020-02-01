from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_view(request):
    return render(request, 'users/login.html')


def login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('learning_logs:index'))
    else:
        return HttpResponseRedirect(reverse('users:login'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
