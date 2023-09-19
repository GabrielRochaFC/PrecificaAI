from django.urls import path
from precificacao.views import index, cadastro_receita

urlpatterns = [
  path('', index, name = 'index'),
  path('cadastro-receita', cadastro_receita, name = 'cadastro_receita')
]