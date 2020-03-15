from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteNovoForm


def listar_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente/listar.html', {'clientes': clientes})


def adicionar_cliente(request):
    form = ClienteNovoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ClienteNovoForm()
    return render(request, 'clientes/cliente/adicionar.html', {'form': form})


def atualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteNovoForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
    return render(request, 'clientes/cliente/adicionar.html', {'form': form})


def detalhar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'clientes/cliente/detalhar.html', {'cliente': cliente})


def remover_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('clientes:listar')


