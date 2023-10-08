from django.contrib import admin
from .models import Servico, Preco, Plano, Cliente


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'criado', 'ativo')

@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('plano', 'criado', 'ativo')

@admin.register(Preco)
class PrecoAdmin(admin.ModelAdmin):
    list_display = ('plano', 'criado', 'ativo')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado', 'ativo')

