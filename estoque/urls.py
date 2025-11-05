from django.urls import path
from .views import ListaProdutos, AddProduto, DeletarProduto, EditarProduto, ListaHistorico, listar_filtrar

urlpatterns = [
    path('produtos/', listar_filtrar, name='produtos_estoque'),
    path('adicionar_produto/', AddProduto.as_view(), name='adicionar_produto'),
    path('<int:pk>/deletar_produto/', DeletarProduto.as_view(), name='deletar_produto'),
    path('<int:pk>/editar_produto/', EditarProduto.as_view(), name='editar_produto'),
    
    # historico
    path('historico/', ListaHistorico.as_view(), name='historico'),

]