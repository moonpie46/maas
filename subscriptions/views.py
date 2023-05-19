from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . import views

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')