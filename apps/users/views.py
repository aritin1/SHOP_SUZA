from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from pyexpat.errors import messages
from django.contrib import messages
from apps.users.forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

@login_required
def account_view(request):
    return render(request, "users/account.html", {"user": request.user})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

User = get_user_model()

def login_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("main")

        messages.error(request, "Неверные учетные данные")

    return render(request, "users/login.html", {"form": form})

def custom_logout(request):
    logout(request)
    return redirect('main')

