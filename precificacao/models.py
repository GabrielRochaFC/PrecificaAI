from django.db import models

# Create your models here.
class Receita(models.Model):
  nome = models.CharField(max_length=255, null=False, blank=False)
  descricao = models.TextField(null=False, blank=False, default='Estou usando precifica aí para precificar minhas receitas!')

  def __str__(self):
    return self.nome

class Ingrediente(models.Model):
  nome = models.CharField(max_length=255, null=False, blank=False)
  quantidade_embalagem = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
  valor_embalagem = models.DecimalField(max_digits=11, decimal_places=2, null=False, blank=False)
  quantidade_usada = models.DecimalField(max_digits=11, decimal_places=2, null=False, blank=False)
  receita = models.ForeignKey('Receita', on_delete=models.CASCADE)
  def valor(self):
    return (self.valor_embalagem / self.quantidade_embalagem) * self.quantidade_usada

  def __str__(self):
    return self.nome