from django.db import models

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
