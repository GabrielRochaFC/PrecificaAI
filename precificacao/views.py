from django.shortcuts import render, redirect, get_object_or_404
from precificacao.models import Receita
from precificacao.forms import ReceitaCadastroForms, IngredienteForm

# Create your views here.
def index(request):
  receita = Receita.objects.all()
  return render(request, 'precificacao/index.html', {'cards' : receita})

def cadastro_receita(request):
  if request.method == "POST":
    form = ReceitaCadastroForms(request.POST)
    if form.is_valid():
      receita = form.save()
      return redirect('listar_ingredientes_da_receita', receita_id=receita.id)
  else:
    form = ReceitaCadastroForms()
  return render(request, 'precificacao/cadastro-receita.html', {"form" : form})

def listar_ingredientes_da_receita(request, receita_id):
  receita = get_object_or_404(Receita, pk=receita_id)
  return render(request, 'precificacao/listar-ingredientes-da-receita.html', {'receita': receita})

def adicionar_ingrediente(request, receita_id):
  receita = get_object_or_404(Receita, pk=receita_id)
  if request.method == 'POST':
    form = IngredienteForm(request.POST)
    if form.is_valid():
      ingrediente = form.save(commit=False)
      ingrediente.receita = receita
      ingrediente.save()
      return redirect('listar_ingredientes_da_receita', receita_id=receita_id)
  else:
    form = IngredienteForm()
  return render(request, 'precificacao/adicionar_ingrediente.html', {'form': form, 'receita': receita})