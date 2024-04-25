from django import forms
from book.models import Livro
from django.forms.widgets import *

class LivroForm (forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo','preco','descricao','imagem','editora','autor','genero']
        labels = {'preco':"Preço"}
        widgets = {'imagem':TextInput(),'descricao':TextInput()}

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update(
            {'placeholder':'Titulo do Livro',
            'class' : 'form-control'}
        )
        self.fields['preco'].widget.attrs.update(
            {'placeholder':'Preço',
            'class' : 'form-control'}
        )
        self.fields['descricao'].widget.attrs.update(
            {'placeholder':'Descrição',
            'class' : 'form-control'}
        )
        self.fields['imagem'].widget.attrs.update(
            {'placeholder':'Nome do arquivo de imagem',
            'class' : 'form-control'}
        )
        self.fields['editora'].widget.attrs.update(
            {'placeholder':'Editora do Livro',
            'class' : 'form-control'}
        )
        self.fields['autor'].widget.attrs.update(
            {'placeholder':'Autor do Livro',
            'class' : 'form-control'}
        )
        self.fields['genero'].widget.attrs.update(
            {'placeholder':'Gênero do Livro',
            'class' : 'form-control'}
        )
