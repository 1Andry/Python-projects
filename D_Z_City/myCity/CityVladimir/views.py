from django.shortcuts import render, redirect
from .models import MyCity
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def index(request):
    city = MyCity.objects.all()
    return render(request, 'CityVladimir/index.html', {'city': city})


def create_user(request):
    if request.method == 'GET':
        return render(request, 'CityVladimir/createuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'CityVladimir/createuser.html', {'form': UserCreationForm(),
                                                                        'error': 'error 1'})
        else:
            return render(request, 'CityVladimir/createuser.html', {'form': UserCreationForm(),
                                                                    'error': 'error 2'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'CityVladimir/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return redirect(request, 'CityVladimir/createuser.html', {'form': AuthenticationForm(),
                                                                      'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('index')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
