from django.db import models
from usuario.models import Usuario
# Create your models here.
class Estoque(models.Model):
    nome_produto = models.CharField(max_length=50)
    qtd_minima = models.IntegerField()
    qtd_produto = models.IntegerField()
    tipo_produto = models.CharField(max_length=20)
    tensao = models.CharField(max_length=10)
    dimensao = models.CharField(max_length=15)
    resolucao_tela = models.CharField(max_length=15)
    armazenamento_gb = models.IntegerField()
    conectividade = models.CharField(max_length=20)

class Historico(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    ESCOLHA_ACAO = [
        ('DELETAR', 'Produto deletado'),
        ('AUMENTAR', 'Produto adicionado ao estoque'),
        ('RETIRADO', 'Produto retirado do estoque'),
        ('ADICIONAR', 'Novo produto'),
    ]
    acao = models.CharField(max_length=20, choices=ESCOLHA_ACAO)
    data_hora = models.DateTimeField(auto_now_add=True)