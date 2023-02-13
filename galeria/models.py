from django.db import models
from datetime import datetime

# Create your models here.
class Fotografia(models.Model):
    # Colunas ou atributos da tabela

    OPCOES_DE_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALAXIA", "Galáxia"),
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
    # blank=True significa que é possível que a gente cadastre uma foto e deixe sem uma
    # imagem. Nesse caso vamos definir uma foto padrão
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return self.nome
