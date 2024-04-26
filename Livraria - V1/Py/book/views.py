from django.shortcuts import render
from book.models import Livro 
from book.forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login as auth_login, authenticate


# Create your views here.
def home(request):
    livro = Livro.objects.order_by('livro_id')
    context = {'livro':livro,
               "UserForm": LoginForm()}
    return render(request, 'home.html', context)

def autores(request):
    livro = Livro.objects.order_by('livro_id')
    context = {'livro':livro}
    return render(request, 'autores.html', context)

def fale(request):
    return render(request, 'fale.html')

def form(request):

    if request.method != 'POST':
        form = LivroForm()
    else:
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

    context = {'form':form}
    return render(request, 'form.html',context)

def sobre(request):
    return render(request, 'sobre.html')

def titulos(request):
    livro = Livro.objects.order_by('livro_id')
    context = {'livro':livro}
    return render(request, 'titulos.html', context)

def professor(request):
    return render(request, 'professor.html')

def abouteditora(request):
    return render(request, 'abouteditora.html')

def imprensa(request):
    return render(request, 'imprensa.html')

def carrinho (request, id):
    livro = Livro.objects.get(livro_id=id)
    context = {'livro':livro}
    return render(request,'carrinho.html',context)

def busca(request):
    Livro = request.GET.get('id', '')
    livros = Livro.objects.filter(livro_id=id)
    return render(request, 'busca.html', {'livros': livros})

def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            auth_login(request, user)
    context = {"LoginForm": LoginForm()}
    return render(request, 'login.html', context)
