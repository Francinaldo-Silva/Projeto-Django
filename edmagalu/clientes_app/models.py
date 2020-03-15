from django.db import models


class Cliente(models.Model):
    email = models.EmailField(max_length=50, db_index=True)
    nome = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome
