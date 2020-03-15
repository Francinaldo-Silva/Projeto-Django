from django.urls import path
from . import views


app_name = 'vendas'

urlpatterns = [
    path('efetuarvenda/', views.efetuar_venda, name='efetuar_venda'),
    path('detalharvenda/<int:id>', views.detalhar_venda, name='detalhar_venda'),
    path('atualizarvenda/<int:id>', views.atualizar_venda, name='atualizar_venda'),
    path('removervenda/<int:id>', views.remover_venda, name='remover_venda'),
    path('', views.listar_vendas, name='listar_vendas'),
]