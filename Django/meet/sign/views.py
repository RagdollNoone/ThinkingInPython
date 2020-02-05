from django.shortcuts import render
from .forms import UserForm


# Create your views here.
def add_user(request):
    if request.method != 'POST':
        form = UserForm()
    else:
        form = UserForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            return True

    return False


