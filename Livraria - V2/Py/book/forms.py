from django import forms
from book.models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo','autor','editora','ano','edicao','paginas','preco','estoque','imagem']
        labels = {
            'titulo':'Título',
            'autor':'Autor',
            'editora':'Editora',
            'ano':'Ano',
            'edicao':'Edição',
            'paginas':'Páginas',
            'preco':'Preço',
            'estoque':'Estoque',
            'imagem':'Imagem'
        }