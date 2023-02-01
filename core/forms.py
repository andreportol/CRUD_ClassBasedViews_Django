from django import forms

from .models import Produto


                            # Herda de ModelForm para trabalhar com banco de dados.
class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'