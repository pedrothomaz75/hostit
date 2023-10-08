from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Servico, Preco, Cliente


class IndexView(TemplateView):
    template_name = 'app/pages/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["servicos"] = Servico.objects.order_by('?').all()
        context["precos"] = Preco.objects.all()
        context["clientes"] = Cliente.objects.order_by('?').all()
        return context


class SobreDetailView(TemplateView):
    template_name = 'app/sobre-detail.html'


class ServicoDetailView(TemplateView):
    template_name = 'app/servico-detail.html'


class PrecoDetailView(TemplateView):
    template_name = 'app/preco-detail.html'


class ContatoDetailView(TemplateView):
    template_name = 'app/contato-detail.html'


