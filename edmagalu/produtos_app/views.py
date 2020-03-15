from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoNovoForm
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produto/listar.html', {'produtos': produtos})

def adicionar_produto(request):
    form = ProdutoNovoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProdutoNovoForm()
    return render(request, 'produtos/produto/adicionar.html',{'form': form})

def atulizar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    form = ProdutoNovoForm(requets.Post or None, instance=produto)
    if form.is_valid():
        form.save()
        return render(request, 'produtos/produto/adicionar.html', {'form' : form})


def detalhar_produto(request,id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produtos/produto/detalhar.html',{'produto':produto})

def remover_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('produtos:listar')
