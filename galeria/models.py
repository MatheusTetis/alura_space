from django.db import models

# Create your models here.
class Fotografia(models.Model):
    # Colunas ou atributos da tabela
    # Especificando que o atributo nome deve ter no máximo
    # 100 caracteres e que não pode ser nulo nem vazio
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'Fotografia [nome={self.nome}]'
