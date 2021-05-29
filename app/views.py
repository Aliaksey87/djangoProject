
# из джанго. ярлыки импорт рендеринга

# Create your views here.
# Создайте здесь свои просмотры.

from django.http import HttpResponse, HttpResponseRedirect
from app.models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.models import User

def register(request):
    user = User.objects.create_user(
        request.POST['login'],
        password=request.POST['password'],
        first_name='aaa',
        last_name='bbb',
        email='a@b.c'
    )
    return HttpResponse('OK')

def register2(request):
    return render(request,
        'register.html',
        {}
    )

def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Ты ек залогинен')

def index2(request):
    return render(request,
        'index2.html',
        {}
    )


def index(request):
    return render(request,
        'index.html',
        {}
    )

# def index(request):
#     return HttpResponse("Это главная страница!")

def page2(request):
    return HttpResponse("Это главная страница222!")

def page3(request):
    return HttpResponse("Это главная страница333!")

def name(request):
    x = spareparts.objects.all()
    return HttpResponse(x[3].cost)



def start_page(request):
    return render(request, 'index.html')


def render_to_response(param, param1):
    pass


def login_user(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return render(request, 'error.html', {})
    else:
        login(request, user)
        return HttpResponseRedirect('/')


# def parol(request):
#     return render(request, 'index.html')

# if request.user.is_authenticated:
#     print("Юзер залогинен")
# else:
#     print("Аноним")

