from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ProdutoModelForm
from .models import Produto

# class based views

class IndexView(ListView):
    model = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all() # Retorna todos os registros do banco de dados.
    print(queryset)
    context_object_name = 'produtos' # nome da lista 'produtos'.

class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')

class UpDateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')

class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('index')