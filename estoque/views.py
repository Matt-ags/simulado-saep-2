from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from .models import Estoque, Historico
from .forms import AddProdutoForm, EditarProdutoForm
from django.urls import reverse_lazy

# Create your views here.
class ListaProdutos(ListView):
    model = Estoque
    template_name = 'estoque/produtos.html'
    context_object_name = 'produtos'

# def lista_produtos(request):
#     produtos = Estoque.objects.all()

#     return render(request, 'estoque/produtos.html', {'produtos', produtos})

class AddProduto(CreateView):
    model = Estoque
    form_class = AddProdutoForm
    template_name = 'estoque/adicionar_produto.html'
    success_url = reverse_lazy('produtos_estoque')

    def form_valid(self, form):
        self.object = form.save()

        Historico.objects.create(
            id_estoque=self.object,
            nome_produto=self.object.nome_produto,
            acao='NOVO_PRODUTO'
        )

        return super().form_valid(form)

class EditarProduto(UpdateView):
    model = Estoque
    form_class = EditarProdutoForm
    template_name = 'estoque/adicionar_produto.html'
    success_url = reverse_lazy('produtos_estoque')

    def form_valid(self, form):
        produto_antigo = Estoque.objects.get(pk=self.object.pk)
        qtd_antiga = produto_antigo.qtd_produto

        response = super().form_valid(form)

        produto_atual = self.object
        qtd_nova = produto_atual.qtd_produto

        if qtd_nova > qtd_antiga:
            acao = 'ENTRADA_PRODUTO'

        elif qtd_nova < qtd_antiga:
            acao = 'SAIDA_PRODUTO'

        else:
            acao = None

        if acao:
            Historico.objects.create(
                id_estoque=self.object,
                nome_produto=self.object.nome_produto,
                acao=acao
            )

        return response

class DeletarProduto(DeleteView):
    model = Estoque
    success_url = reverse_lazy('produtos_estoque')
        
    def get(self, request, *args, **kwargs):
        # Força a exclusão direta, sem template
        self.object = self.get_object()

        Historico.objects.create(
            # id_usuario='null',   # ou outro campo, se seu user não for o padrão
            id_estoque=self.object,
            nome_produto=self.object.nome_produto,
            acao='DELETAR'
        )

        self.object.delete()
        return redirect(self.success_url)

class ListaHistorico(ListView):
    model = Historico
    template_name = 'estoque/historico.html'
    context_object_name = 'historico'