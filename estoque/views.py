from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from .models import Estoque, Historico
from usuario.models import Usuario
from .forms import AddProdutoForm, EditarProdutoForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
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


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = self
        self.action = 'add'  # ← aqui definimos o valor
        return context


    def form_valid(self, form):
        self.object = form.save()




        usuario_autenticado = None # como é "create view", tem que ser dessa forma esquisita
        django_user = getattr(self.request, 'user', None)
        if django_user and django_user.is_authenticated:
            usuario_autenticado = django_user


        Historico.objects.create(
            id_estoque=self.object,
            id_usuario=usuario_autenticado,
            nome_produto=self.object.nome_produto,
            acao='NOVO_PRODUTO'
        )


        return super().form_valid(form)


class EditarProduto(UpdateView):
    model = Estoque
    form_class = EditarProdutoForm
    template_name = 'estoque/adicionar_produto.html'
    success_url = reverse_lazy('produtos_estoque')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = self
        self.action = 'editar'  # ← aqui definimos o valor
        return context


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
            usuario_autenticado = None
            django_user = getattr(self.request, 'user', None)
            if django_user and django_user.is_authenticated:
                usuario_autenticado = django_user


            Historico.objects.create(
                id_estoque=self.object,
                id_usuario=usuario_autenticado,
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




        usuario_autenticado = None
        django_user = getattr(request, 'user', None)
        if django_user and django_user.is_authenticated:
            usuario_autenticado = django_user


        Historico.objects.create(
            id_usuario=usuario_autenticado,
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
    ordering = ['nome_produto']


    def get_queryset(self):
        queryset = super().get_queryset()


        nome = self.request.GET.get('nome')
        acao = self.request.GET.get('acao')
        data = self.request.GET.get('data')


        if nome:
            queryset = queryset.filter(nome_produto__icontains=nome)


        if acao:
            queryset = queryset.filter(acao__iexact=acao)


        if data:
            queryset = queryset.filter(data_hora__date=data)


        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['acoes_disponiveis'] = Historico.ESCOLHA_ACAO
        return context


@login_required(login_url='/login')
def listar_filtrar(request):
    busca = request.GET.get('q')
    tipo = request.GET.get('tipo')


    produtos = Estoque.objects.all()


    if busca:
        produtos = produtos.filter(nome_produto__icontains=busca)


    if tipo:
        produtos = produtos.filter(tipo_produto=tipo)


    produtos = produtos.order_by('nome_produto')


    return render(request, 'estoque/produtos.html', {
        "usuario": request.user,
        "produtos": produtos,
    })


