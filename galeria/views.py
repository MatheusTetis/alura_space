from django.shortcuts import get_object_or_404, render
from galeria.models import Fotografia
from usuarios.models import Favoritos
from django.contrib.auth.models import User
from django.db.models import Case, Count, Exists, IntegerField, OuterRef, Q, When
from unidecode import unidecode
from django.db.models import Prefetch


# Create your views here.
def index(request):
    # Criando a função "faoritada" para verificar se a foto foi favoritada
    # (se ela existe na tabela Favoritos) usando o comando
    # fotografia.fotofavoritada dentro do Django Template "_card.html"
    favoritada = Favoritos.objects.filter(
        fotografia=OuterRef('pk'),
        usuario=request.user.id,
        is_favorito=True,
    )

    # Criando a função "nlikes" para retornar o número de linhas da foto
    # com "is_favorito" True ao usar o comando fotografia.nlikes
    # dentro do Django Template "_card.html"
    nlikes = Favoritos.objects.filter(
        fotografia_id=OuterRef('pk'),
        is_favorito=True,
    ).annotate(numerolikes=Count('id'))

    # Filtrando apenas fotos publicadas
    fotografias = Fotografia.objects.filter(publicada=True)
    # Adicionando a função "fotofavoritada"
    fotografias = fotografias.annotate(fotofavoritada=Exists(favoritada))
    # Adicionando a função "nlikes" que vai contar quantos is_favorito = True
    # contem na tabela de Favoritos usando o related_name "fotoid" como ponte
    fotografias = fotografias.annotate(
        nlikes=Count(
            'fotoid__is_favorito',
            filter = Q(fotoid__is_favorito=True)
        )
    )

    # Criando o Queryset "favoritos" filtrando o usuário que fez a requisição
    # e trazendo apenas as fotos favoritadas
    favoritos = Favoritos.objects.filter(
        usuario=request.user.id,
        is_favorito=True,
    )
    
    # Carregando todas as opções de categorias registradas no Model Fotografias
    # para disponibilizar nos botões de busca por Categoria
    categorias = []
    for conjunto in Fotografia.OPCOES_DE_CATEGORIA:
        categorias.append(conjunto[1])

    return render(
        request,
        template_name='galeria/index.html',
        context={'cards': fotografias, 'categorias': categorias, 'favoritos': favoritos}
    )

def imagem(request, foto_id):
    # pk = Primary Key
    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    return render(
        request,
        template_name='galeria/imagem.html',
        context={'fotografia': fotografia}
    )

def buscar(request):
    # Criando a função "faoritada" para verificar se a foto foi favoritada
    # (se ela existe na tabela Favoritos) usando o comando
    # fotografia.fotofavoritada dentro do Django Template "_card.html"
    favoritada = Favoritos.objects.filter(
        fotografia=OuterRef('pk'),
        usuario=request.user.id,
        is_favorito=True,
    )

    # Criando a função "nlikes" para retornar o número de linhas da foto
    # com "is_favorito" True ao usar o comando fotografia.nlikes
    # dentro do Django Template "_card.html"
    nlikes = Favoritos.objects.filter(
        fotografia_id=OuterRef('pk'),
        is_favorito=True,
    ).annotate(numerolikes=Count('id'))

    # Filtrando apenas fotos publicadas
    fotografias = Fotografia.objects.filter(publicada=True)
    # Adicionando a função "fotofavoritada"
    fotografias = fotografias.annotate(fotofavoritada=Exists(favoritada))
    # Adicionando a função "nlikes" que vai contar quantos is_favorito = True
    # contem na tabela de Favoritos usando o related_name "fotoid" como ponte
    fotografias = fotografias.annotate(
        nlikes=Count(
            'fotoid__is_favorito',
            filter = Q(fotoid__is_favorito=True)
        )
    )

    # Criando o Queryset "favoritos" filtrando o usuário que fez a requisição
    # e trazendo apenas as fotos favoritadas
    favoritos = Favoritos.objects.filter(
        usuario=request.user.id,
        is_favorito=True,
    )

    # Carregando as categorias para renderizar as tags
    categorias = []
    for conjunto in Fotografia.OPCOES_DE_CATEGORIA:
        categorias.append(conjunto[1])

    # Conferindo se o parâmetro buscar está na url
    if "buscar" in request.GET:
        # Pegando o que está sendo passado no parâmetro 'buscar' da url
        nome_a_buscar = unidecode(request.GET['buscar'])
        if nome_a_buscar:
            # Vai buscar no banco de dados se o parâmetro 'nome_a_buscar'
            # está contido no campo 'nome'
            print('Filtrando nome')
            fotografias = fotografias.filter(
                Q(nome__icontains=nome_a_buscar) | Q(nome=nome_a_buscar) |
                Q(categoria__icontains=nome_a_buscar) | Q(categoria=nome_a_buscar)
            )

    return render(
        request,
        template_name='galeria/buscar.html',
        context={'cards': fotografias, 'categorias': categorias, 'favoritos': favoritos}
    )