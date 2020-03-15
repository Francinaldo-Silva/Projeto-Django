
from django.shortcuts import render, get_object_or_404, redirect
from .models import NotaFiscal
from .forms import EfetuarVendaForm


def listar_vendas(request):
    vendas = NotaFiscal.objects.all()
    return render(request, 'vendas/venda/listar.html', {'vendas': vendas})


def efetuar_venda(request):
    form = EfetuarVendaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EfetuarVendaForm()
    return render(request, 'vendas/venda/efetuar_venda.html', {'form': form})


def detalhar_venda(request, id):
    nota_fiscal = get_object_or_404(NotaFiscal, id=id)
    return render(request, 'vendas/venda/detalhar.html', {'nota_fiscal': nota_fiscal})


def atualizar_venda(request, id):
    nota_fiscal = get_object_or_404(NotaFiscal, id=id)
    form = EfetuarVendaForm(request.POST or None, instance=nota_fiscal)
    if form.is_valid():
        form.save()
    return render(request, 'vendas/venda/efetuar_venda.html', {'form': form})


def remover_venda(request, id):
    nota_fiscal = get_object_or_404(NotaFiscal, id=id)
    nota_fiscal.delete()
    return redirect('vendas:listar_vendas')
