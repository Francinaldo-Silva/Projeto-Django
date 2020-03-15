from django.db import models


class Produto(models.Model):
    codigo = models.CharField(max_length=20, db_index=True)
    nome = models.CharField(max_length=100, blank=False)
    descricao = models.TextField(max_length=200, blank=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome
