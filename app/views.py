from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'app/pages/index.html'


class SobreDetailView(TemplateView):
    template_name = 'app/sobre-detail.html'


class ServicoDetailView(TemplateView):
    template_name = 'app/servico-detail.html'


class PrecoDetailView(TemplateView):
    template_name = 'app/preco-detail.html'


class ContatoDetailView(TemplateView):
    template_name = 'app/contato-detail.html'