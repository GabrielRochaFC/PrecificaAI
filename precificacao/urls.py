from django.urls import path
from precificacao.views import index, cadastro_receita, listar_ingredientes_da_receita, adicionar_ingrediente, mao_de_obra

urlpatterns = [
  path('', index, name = 'index'),
  path('cadastro-receita', cadastro_receita, name = 'cadastro_receita'),
  path('listar-ingredientes-da-receita/<int:receita_id>', listar_ingredientes_da_receita, name = 'listar_ingredientes_da_receita'),
  path('adicionar-ingrediente/<int:receita_id>', adicionar_ingrediente, name= 'adicionar_ingrediente'),
  path('mao-de-obra', mao_de_obra, name='mao_de_obra')
]