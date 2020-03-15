from django import forms
from .models import Produto

class ProdutoNovoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'codigo',
            'nome',
            'descricao'
        ]