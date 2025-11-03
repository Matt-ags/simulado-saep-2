from django.urls import path
from .views import ListaProdutos, AddProduto, DeletarProduto, lista_produtos

urlpatterns = [
    path('produtos/', lista_produtos, name='produtos_estoque'),
    path('adicionar_produto/', AddProduto.as_view(), name='adicionar_produto'),
    path('<int:pk>/deletar_produto/', DeletarProduto.as_view(), name='deletar_produto')
]