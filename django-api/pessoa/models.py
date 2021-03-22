from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=50)
    interesse = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'pessoas'
