from django.db import models


class Feira(models.Model):
    longi = models.CharField(max_length=15, blank=True, default='')
    lat = models.CharField(max_length=15, blank=True, default='')
    setcens = models.CharField(max_length=20, blank=True, default='')
    areap = models.CharField(max_length=20, blank=True, default='')
    coddist = models.IntegerField(blank=True, null=True)
    distrito = models.CharField(max_length=20, blank=True, default='')
    codsubpref = models.IntegerField(blank=True, null=True)
    subprefe = models.CharField(max_length=40, blank=True, default='')
    regiao5 = models.CharField(max_length=20, blank=True, default='')
    regiao8 = models.CharField(max_length=20, blank=True, default='')
    nome_feira = models.CharField(max_length=40, blank=True, default='')
    registro = models.CharField(max_length=10, blank=True, default='')
    logradouro = models.CharField(max_length=40, blank=True, default='')
    numero = models.CharField(max_length=15, blank=True, default='')
    bairro = models.CharField(max_length=40, blank=True, default='')
    referencia = models.CharField(max_length=40, blank=True, default='')

    def __str__(self):
        return 'nome: {}, bairro: {}'.format(self.nome_feira, self.bairro)
