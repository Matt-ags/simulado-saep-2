from django import forms
from .models import Estoque

class AddProdutoForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = '__all__'