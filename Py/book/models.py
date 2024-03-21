from django.db import models

# Create your models here.
class Livro (models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano = models.IntegerField()
    edicao = models.IntegerField()
    paginas = models.IntegerField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    estoque = models.IntegerField()
    def __str__(self):
        return self.titulo