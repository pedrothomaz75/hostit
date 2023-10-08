from django.urls import path
from .views import (
    IndexView, SobreDetailView, ServicoDetailView,
    PrecoDetailView, ContatoDetailView
)

urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
    path('sobre/', SobreDetailView.as_view(), name='sobre-datail'),
    path('servico/', ServicoDetailView.as_view(), name='servico-detail'),
    path('precos/', PrecoDetailView.as_view(), name='preco-detail'),
    path('contato/', ContatoDetailView.as_view(), name='contato-detail')
]
