from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from .models import Estoque, Historico
from .forms import AddProdutoForm
from django.urls import reverse_lazy

# Create your views here.
class ListaProdutos(ListView):
    model = Estoque
    template_name = 'estoque/produtos.html'
    context_object_name = 'produtos'

def lista_produtos(request):
    produtos = Estoque.objects.all()

    if 'adicionar':
        produtos.qtd_produto += 1
    elif 'reduzir':
        produtos.qtd_produto -= 1

    return render(request, 'estoque/produtos.html', {'produtos', produtos})

class AddProduto(CreateView):
    model = Estoque
    form_class = AddProdutoForm
    template_name = 'estoque/adicionar_produto.html'
    success_url = reverse_lazy('produtos_estoque')

class DeletarProduto(DeleteView):
    model = Estoque
    success_url = reverse_lazy('produtos_estoque')

    def get(self, request, *args, **kwargs):
        # Força a exclusão direta, sem template
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)