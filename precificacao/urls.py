from django.urls import path
from precificacao.views import index

urlpatterns = [
  path('', index)
]