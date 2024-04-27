from django import forms
from book.models import Livro
from django.forms.widgets import *
from django.contrib.auth.models import User

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

class LoginForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {'p   assword':PasswordInput()}
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder':'Nome de Usuário',
            'class' : 'form-control'} )
        
        self.fields['password'].widget.attrs.update(
            {'placeholder':'Senha',
            'class' : 'form-control',})

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password', 'email','first_name','last_name']
        widgets = {'email':EmailInput(),'password':PasswordInput()}
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder':'Nome de Usuário',
            'class' : 'form-control'} )
        self.fields['password'].widget.attrs.update(
            {'placeholder':'Senha',
            'class' : 'form-control',})
        self.fields['email'].widget.attrs.update(
            {'placeholder':'Email',
            'class' : 'form-control',})
        self.fields['first_name'].widget.attrs.update(
            {'placeholder':'Nome',
            'class' : 'form-control',})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder':'Sobrenome',
            'class' : 'form-control',})

class ClienteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','cpf', 'endereço','numero','complemento','bairro','cidade', 'estado','cep','telefone', 'celular','email','password', 'confirm_password','como_soube']
        widgets = {'email':EmailInput(),'password':PasswordInput()}
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder':'Nome de Usuário', 'class': 'form-control'} )
        self.fields['cpf'].widget.attrs.update(
            {'placeholder':'CPF',
            'class' : 'form-control',})
        self.fields['endereco'].widget.attrs.update(
            {'placeholder':'Endereço',
            'class' : 'form-control',})
        self.fields['numero'].widget.attrs.update(
            {'placeholder':'Numero',
            'class' : 'form-control',})
        self.fields['complemento'].widget.attrs.update(
            {'placeholder':'Complemento',
            'class' : 'form-control',})
        self.fields['bairro'].widget.attrs.update(
            {'placeholder':'Bairro',
            'class' : 'form-control',})
        self.fields['cidade'].widget.attrs.update(
            {'placeholder':'Cidade',
            'class' : 'form-control',})
        self.fields['estado'].widget.attrs.update(
            {'placeholder':'Estado',
            'class' : 'form-control',})
        self.fields['cep'].widget.attrs.update(
            {'placeholder':'CEP',
            'class' : 'form-control',})
        self.fields['telefone'].widget.attrs.update(
            {'placeholder':'Telefone',
            'class' : 'form-control',})
        self.fields['celular'].widget.attrs.update(
            {'placeholder':'Celular',
            'class' : 'form-control',})
        self.fields['email'].widget.attrs.update(
            {'placeholder':'Email',
            'class' : 'form-control',}) 
        self.fields['password'].widget.attrs.update(
            {'placeholder':'Senha',
            'class' : 'form-control',})
        self.fields['confirm_password'].widget.attrs.update(
            {'placeholder':'Confirme sua Senha',    
            'class' : 'form-control',})
        self.fields['como_soube'].widget.attrs.update(           
            {'placeholder':'Como soube do site?',
            'class' : 'form-control',})
        
