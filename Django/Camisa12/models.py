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
