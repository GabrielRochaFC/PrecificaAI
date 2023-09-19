from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'precificacao/index.html')

def cadastro_receita(request):
  return render(request, 'precificacao/cadastro-receita.html')