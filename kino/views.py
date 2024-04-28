from django.shortcuts import render,redirect
from .models import *
import random

def index(req):
    film = modelKino.objects.all()
    actor = modelActor.objects.all()
    randomFilm = random.choice(film)
    data = {'film':film, 'actor':actor, 'random':randomFilm}
    return render(req, 'index.html', data)


from django.views import generic

class kinolist(generic.ListView):
    model = modelKino
    paginate_by = 2


class actorlist(generic.ListView):
    model = modelActor
    paginate_by = 2

class directorlist(generic.ListView):
    model = modelDirector
    paginate_by = 2

class kinoDetail(generic.DetailView):
    model = modelKino


class actorDetail(generic.DetailView):
    model = modelActor

class directorDetail(generic.DetailView):
    model = modelDirector

from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def register(req):
    print(1)
    if req.POST:
        print(2)
        forma = formRegister(req.POST)
        if forma.is_valid():
            print(3)
            k1=forma.cleaned_data.get('username')
            k2 = forma.cleaned_data.get('password1')
            k3 = forma.cleaned_data.get('email')
            k4 = forma.cleaned_data.get('first_name')
            k5 = forma.cleaned_data.get('last_name')
            User.objects.create_user(username=k1, password= k2) # создает юзера
            #user = authenticate(username=k1, password= k2)
            user = User.objects.get(username=k1)  # находит юзера
            user.email =k3
            user.first_name = k4
            user.last_name =k5
            user.save()
            modelProfile.objects.create(balance=1000, podpiska_id=1, user_id=user.id)
            login(req,user)  # вход пользователя на сайт
            return redirect('home')  # переходит на главную
    else:
        forma = formRegister()
    data = {'forma' : forma}
    return render(req, 'registration/registration.html', data)


def profile(req):
    return render(req, 'kabinet.html')


def profileChange(req):
    forma = formPodpiska()
    data = {'form':forma}
    if req.POST:
        k1=req.POST.get('item')
        print(k1)
        user = User.objects.get(id=req.user.id)
        user.modelprofile.podpiska_id = k1
        balance = user.modelprofile.balance
        podpiska=modelPodpiska.objects.get(id=k1)
        if balance<podpiska.price:
            message='Недостаточно средств!'
            data = {'form': forma, 'message':message}
        else:
            k2=balance-podpiska.price
            user.modelprofile.balance= k2
            user.modelprofile.save()
            return redirect('kabinet')
    return render(req, 'kabinet.html',data)


def otziv(req, kinoid):
    print(kinoid)
    if req.POST:
        k1 = req.user.username
        k2 = req.POST.get('text')
        k3 = req.user.id
        film = modelKino.objects.get(id=kinoid)
        print(k1,k2,k3)
        modelOtziv.objects.create(text=k2, user_id=k3,film_id=kinoid)
        return redirect('onekino',film.genre, kinoid)
    return redirect('home')


















