from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
#from galeria.models import Fotografia

# Create your models here.
class Favoritos(models.Model):
    # Colunas ou atributos da tabela
    # Especificando que o atributo nome deve ter no máximo
    # 100 caracteres e que não pode ser nulo nem vazio
    usuario = models.ForeignKey(
        to = User,
        on_delete = models.CASCADE,
        null = False,
        blank = False,
        # Forma que a gente tem de poder localizar melhor
        # qual que é a tabela
        related_name = 'userid',
    )
    #fotografia = models.ForeignKey(
    #    to = Fotografia,
    #    on_delete = models.CASCADE,
    #    null = False,
    #    blank = False,
    #    # Forma que a gente tem de poder localizar melhor
    #    # qual que é a tabela
    #    related_name = 'fotoid'
    #)
    #usuario_id = models.IntegerField(null=False, blank=False)
    fotografia = models.IntegerField(null=False, blank=False)
    is_favorito = models.BooleanField(null=False, blank=False)
    data_like = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return self.nome