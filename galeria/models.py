from django.db import models
from datetime import datetime

# Create your models here.
class Fotografia(models.Model):
    # Colunas ou atributos da tabela

    OPCOES_DE_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("AGLOMERADO", "Aglomerado"),
        ("PLANETA", "Planeta"),
        ("LUA", "Lua"),
    ]

    # Especificando que o atributo nome deve ter no máximo
    # 100 caracteres e que não pode ser nulo nem vazio
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_DE_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return f'Fotografia [nome={self.nome}]'
