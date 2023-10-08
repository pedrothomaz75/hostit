from django.db import models
from stdimage.models import StdImageField

class Base(models.Model):
    criado = models.DateTimeField('criado', auto_now_add=True)
    modificado = models.DateTimeField('atualizado', auto_now=True)
    ativo = models.BooleanField('ativo ?', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    imagem = StdImageField('imagem', upload_to='media/servicos', variations={'thumb': {'width': 196, 'height': 168, 'crop': True}})

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico
    


class Plano(Base):
    plano = models.CharField('Plano', max_length=50) 

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'

    def __str__(self):
        return self.plano
    

class Preco(Base):
    preco = models.CharField('Preço', max_length=100)
    plano = models.ForeignKey('app.Plano', verbose_name='Plano', on_delete=models.CASCADE)
    descricao = models.TextField('Descrição', max_length=200)

    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'

    def __str__(self):
        return self.preco



class Cliente(Base):
    nome = models.CharField('Nome', max_length=100)
    plano = models.ForeignKey('app.Plano', verbose_name='Plano', on_delete=models.CASCADE)
    avaliacao = models.TextField('Avaliação', max_length=300)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


    

    
    

