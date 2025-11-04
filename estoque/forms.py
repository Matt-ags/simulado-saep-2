from django import forms
from .models import Estoque, Historico

class AddProdutoForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = '__all__'

class EditarProdutoForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['qtd_produto']