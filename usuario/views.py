from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User # na docs, mostra que já temos "criado", usamos essa model como base :D
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.urls import reverse
# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = User.objects.filter(username=nome).first()
       
        if user:
            messages.error(request, "Já existe um usuário com este nick, experimente outro!")
            return redirect('cadastro')        
       
        user = User.objects.create_user(username=nome, password=senha)
        user.save()
        login_django(request, user)


    return redirect('produtos_estoque')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')


        user = authenticate(username=nome, password=senha)


        if user:
            login_django(request, user)
            return redirect('produtos_estoque')
           
        else:
            messages.error(request, "Usuário ou senha incorretos. Verifique as informações.")
            return redirect('login')        
       
def logout_view(request):
    logout(request)
    return redirect('/login')




@login_required(login_url='/login/')
def plataforma(request):
    return HttpResponse("teste")

