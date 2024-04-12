from django.db import models

class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    #quebra
    endereco = models.CharField(max_length=200)
    #separa
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    #senha, ...

    def __str__(self):
        return self.nome

class Livro(models.Model):
    livro_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    #quebra
    autor = models.CharField(max_length=100)
    #quebra
    editora = models.CharField(max_length=100)
    #quebra
    genero = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.TextField(max_length=5000)
    descricao = models.TextField(max_length=5000)

    def __str__(self):
        return self.titulo

class Venda(models.Model):
    venda_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_venda = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venda {self.venda_id} - Cliente: {self.cliente.nome}"

class ItemVenda(models.Model):
    itemvenda_id = models.AutoField(primary_key=True)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"Item {self.itemvenda_id} - Livro: {self.livro.titulo}, Quantidade: {self.quantidade}"
