from django.db import models
from usuario.models import Usuario
# Create your models here.
class Estoque(models.Model):
    nome_produto = models.CharField(max_length=50)
    qtd_minima = models.IntegerField()
    qtd_produto = models.IntegerField()

    ESCOLHA_TIPO_PRODUTO = [
        ('smartphone', 'Celular'),
        ('notebook', 'Notebook'),
        ('smart_tv', 'Smart TV')
    ]

    tipo_produto = models.CharField(max_length=20, choices=ESCOLHA_TIPO_PRODUTO)
    tensao = models.CharField(max_length=10)
    dimensao = models.CharField(max_length=15)
    resolucao_tela = models.CharField(max_length=15)
    armazenamento_gb = models.IntegerField()
    conectividade = models.CharField(max_length=20)

class Historico(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    id_estoque = models.ForeignKey(Estoque, on_delete=models.SET_NULL, null=True)

    nome_produto = models.CharField(max_length=50, blank=True, null=True)

    ESCOLHA_ACAO = [
        ('DELETAR', 'Produto deletado'),
        ('ENTRADA_PRODUTO', 'Produto adicionado ao estoque'),
        ('SAIDA_PRODUTO', 'Produto retirado do estoque'),
        ('NOVO_PRODUTO', 'Novo produto'),
    ]

    acao = models.CharField(max_length=20, choices=ESCOLHA_ACAO)
    data_hora = models.DateTimeField(auto_now_add=True)