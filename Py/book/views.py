from django.shortcuts import render
from book.models import Livro 

# Create your views here.
def home(request):
    livro = Livro.objects.order_by('id')
    context = {'livro':livro}
    return render(request, 'home.html', context)

def autores(request):
    return render(request, 'autores.html')

def fale(request):
    return render(request, 'fale.html')

def imprensa(request):
    return render(request, 'imprensa.html')

def sobre(request):
    return render(request, 'sobre.html')

def titulos(request):
    return render(request, 'titulos.html')

def professor(request):
    return render(request, 'professor.html')