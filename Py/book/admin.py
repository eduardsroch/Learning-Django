from django.contrib import admin
from book.models import Livro
from book.models import Autor
from book.models import Editora

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Editora)



