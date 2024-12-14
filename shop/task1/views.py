from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.

from .forms import User


def registration(request):
    info={}
    global form
    buyers = Buyer.objects.all()
    users=[]
    for i in buyers:
        users.append(i.name)
    if request.method == 'POST':
        form = User(request.POST)
        s=[]
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            s.append(name)
            s.append(age)
            s.append(password)
            s.append(repeat_password)
        if s[0] in users:
            return HttpResponse('This user yet was')
        if s[2]!=s[3]:
            return HttpResponse('wrong password')
        Buyer.objects.create(name=s[0], balance=0, age=s[1])
        return HttpResponse('all was successful')
    else:
        form = User()
    return render(request, 'registration.html', {'form': form})

def shop(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'shop.html', context)


def main(request):
    return render(request, 'main.html')


def shopping_cart(request):
    return render(request, 'shopping_cart.html')
