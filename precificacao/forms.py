from django import forms
from precificacao.models import Receita, Ingrediente
from django.core.exceptions import ValidationError

class ReceitaCadastroForms(forms.ModelForm):
  class Meta:
    model = Receita
    labels = {
      "nome" : "Nome da receita",
    }
    fields = ["nome","descricao"]
    widgets = {
      "nome" : forms.TextInput(attrs={
        "class" : "form-control"
      }),
      "descricao" : forms.Textarea(attrs={
        "class" : "form-control"
      })
    }
class IngredienteForm(forms.ModelForm):
  class Meta:
    model = Ingrediente
    fields = ['nome', 'quantidade_embalagem', 'valor_embalagem', 'quantidade_usada']
    labels = {
      "nome" : "Nome do ingrediente",
      "quantidade_embalagem" : "Quantidade da embalagem",
      "valor_embalagem" : "Valor da embalagem",
      "quantidade_usada" : "Quantidade usada"
    }
    widgets = {
      "nome" : forms.TextInput(attrs={"class" : "form-control"}),
      "quantidade_embalagem" : forms.NumberInput(attrs={"class" : "form-control"}),
      "valor_embalagem" : forms.NumberInput(attrs={"class" : "form-control"}),
      "quantidade_usada" : forms.NumberInput(attrs={"class" : "form-control"})
    }
  def clean_quantidade_embalagem(self):
    quantidade_embalagem = self.cleaned_data['quantidade_embalagem']
    if quantidade_embalagem < 0:
      raise ValidationError("A quantidade da embalagem não pode ser negativa.")
    return quantidade_embalagem

  def clean_valor_embalagem(self):
    valor_embalagem = self.cleaned_data['valor_embalagem']
    if valor_embalagem < 0:
      raise ValidationError("O valor da embalagem não pode ser negativo.")
    return valor_embalagem

  def clean_quantidade_usada(self):
    quantidade_usada = self.cleaned_data['quantidade_usada']
    if quantidade_usada < 0:
      raise ValidationError("A quantidade usada não pode ser negativa.")
    return quantidade_usada