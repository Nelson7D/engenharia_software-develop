from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate, login, logout, update_session_auth_hash
)
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .decorators import *

from django.conf import settings
from .forms import *
from .models import *



# Create your views here.
@admin_only
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {"latest_question_list": 'latest_question_list'}
    return render(request, "management/index.html", context)

@admin_only
def create_employer(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Conta criada com sucesso: {user.username}')
            return HttpResponseRedirect(reverse('accounts:user_login'))
    context = {'form':form}

    return render(request, "management/index.html", context)

@unautenticate_user
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('management:index'))
        else:
            messages.info(request, 'Username ou palavra-passe incorreta')
            return render(request, 'management/login.html')
    context = {}
    return render(request, 'management/login.html',context)

@login_required
def logout_user(request):
    logout(request)
    return sign_in(request)

def cadastro_produto(request):

    context = {}
    return render(request, 'management/cadastro-produto.html',context)


def dashboard(request):

    context = {}
    return render(request, 'management/dashboard.html',context)

def tabela_sem_dados(request):

    context = {}
    return render(request, 'management/tabela-sem-dados.html',context)


def pesquisa_produtos(request):

    context = {}
    return render(request, 'management/pesquisa-produtos.html',context)


def login_page(request):

    context = {}
    return render(request, 'management/login.html',context)

def cadastro_page(request):

    context = {}
    return render(request, 'management/cadastro.html',context)

def pagina_vazia(request):

    context = {}
    return render(request, 'management/pagina-vazia.html',context)

def esqueceu_a_senha(request):
    context = {}
    return render(request, 'management/esqueceu-a-senha.html',context)

def cadastro_funcionario(request):
    context = {}
    return render(request, 'management/cadastro-funcionario.html',context)

def error_403(request):
    context = {}
    return render(request, 'management/403.html',context)

def error_404(request):
    context = {}
    return render(request, 'management/404.html',context)

def error_500(request):
    context = {}
    return render(request, 'management/500.html',context)
