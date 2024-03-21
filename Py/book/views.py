from django.shortcuts import render
from book.models import Livro 

# Create your views here.
def home(request):
    livro = Livro.objects.order_by('id')
    context = {'livro':livro}
    return render(request, 'home.html', context)

def autores(request):
    livro = Livro.objects.order_by('id')
    context = {'livro':livro}
    return render(request, 'autores.html',context)

def fale(request):
    return render(request, 'fale.html')