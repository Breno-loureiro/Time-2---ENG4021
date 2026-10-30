from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 1) Banco de dados de tamanhos de camisa
class Tamanho(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField()          # ex.: P, M, G, GG
    largura = models.IntegerField()    # largura da camisa em cm
    altura = models.IntegerField()     # altura da camisa em cm

    class Meta:
        managed = True
        db_table = 'Tamanho'
        ordering = ['id']

    def __str__(self):
        '''
        Retorna o texto que aparece na interface de admin.
        '''
        return "Tamanho: " + self.nome

# 2) Banco de dados de notas de conservação da camisa
class NotaConservacao(models.Model):
    id = models.AutoField(primary_key=True)
    nota = models.IntegerField()       # de 1 a 5
    titulo = models.TextField()        # ex.: Nova com etiqueta
    descricao = models.TextField()     # ex.: sem manchas e sem desgaste

    class Meta:
        managed = True
        db_table = 'NotaConservacao'
        ordering = ['nota']

    def __str__(self):
        '''
        Retorna o texto que aparece na interface de admin.
        '''
        return "Nota " + str(self.nota) + ": " + self.titulo

# 3) Banco de dados de times
class Time(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField()      # ex.: Fluminense
    sigla = models.TextField()     # ex.: FLU
    liga = models.TextField()      # ex.: Brasileirão Série A

    class Meta:
        managed = True
        db_table = 'Time'
        ordering = ['nome']

    def __str__(self):
        '''
        Retorna o texto que aparece na interface de admin.
        '''
        return "Time: " + self.nome

# 4) Banco de dados de ligas
class Liga(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField()          # ex.: Brasileirão Série A
    pais = models.TextField()          # ex.: Brasil
    divisao = models.IntegerField()    # 1 ou 2

    class Meta:
        managed = True
        db_table = 'Liga'
        ordering = ['nome']

    def __str__(self):
        '''
        Retorna o texto que aparece na interface de admin.
        '''
        return "Liga: " + self.nome

# 5) Banco de dados de confederações
class Confederacao(models.Model):
    id = models.AutoField(primary_key=True)
    sigla = models.TextField()         # ex.: CONMEBOL
    continente = models.TextField()    # ex.: América do Sul

    class Meta:
        managed = True
        db_table = 'Confederacao'
        ordering = ['sigla']

    def __str__(self):
        '''
        Retorna o texto que aparece na interface de admin.
        '''
        return "Confederação: " + self.sigla

# 6) Banco de dados de produtos
class Produto(models.Model):

    CATEGORIAS = [
        ("FUTEBOL", "Futebol"),
        ("NBA", "NBA"),
        ("NFL", "NFL"),
    ]

    id = models.AutoField(
        primary_key=True
    )

    nome = models.CharField(
        max_length=200
    )

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS
    )

    marca = models.CharField(
        max_length=100,
        blank=True
    )

    modelo = models.CharField(
        max_length=100,
        blank=True
    )

    ano = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    descricao = models.TextField(
        blank=True
    )

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    imagem = models.URLField(
        blank=True
    )

    ativo = models.BooleanField(
        default=True
    )

    tamanho = models.ForeignKey(
        Tamanho,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="produtos"
    )

    conservacao = models.ForeignKey(
        NotaConservacao,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="produtos"
    )

    time = models.ForeignKey(
        Time,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="produtos"
    )

    vendedor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="produtos"
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )


    class Meta:
        managed = True
        db_table = "Produto"
        ordering = ["-criado_em"]


    def __str__(self):
        return self.nome
