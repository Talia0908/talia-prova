from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    dt_nasc = models.DateField()
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=1)

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    

class CarrinhoDeCompras(models.Model):
    cor = models.CharField(max_length=20)
    tamanho = models.CharField(max_length=20)
    setor = models.CharField(max_length=30)        
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)




