from django.contrib import admin
from precificacao.models import Receita, Ingrediente


class ListandoReceitas(admin.ModelAdmin):
  list_display = ('nome',)
  list_display_links = ('nome',)
  search_fields = ('nome',)

class ListandoIngredientes(admin.ModelAdmin):
  list_display = ('nome', 'quantidade_embalagem', 'valor_embalagem', 'quantidade_usada')
  list_display_links = ('nome',)
  search_fields = ('nome',)

# Register your models here.
admin.site.register(Receita, ListandoReceitas)
admin.site.register(Ingrediente, ListandoIngredientes)