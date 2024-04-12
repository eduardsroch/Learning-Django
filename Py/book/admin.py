from django.contrib import admin
from book.models import Livro
from book.models import Venda
from book.models import Cliente
from book.models import ItemVenda


admin.site.register(Livro)
admin.site.register(Venda)
admin.site.register(Cliente)
admin.site.register(ItemVenda)





