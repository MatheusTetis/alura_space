from django.shortcuts import get_object_or_404, render
from galeria.models import Fotografia
from usuarios.models import Favoritos
from django.contrib.auth.models import User
from django.db.models import Q
from unidecode import unidecode


# Create your views here.
def index(request):
    fotografias = Fotografia.objects.filter(publicada=True)
    favoritos = Favoritos.objects.filter(usuario=request.user.id)
    print(Fotografia.objects.select_related('usuario').all())

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
    fotografias = Fotografia.objects.filter(publicada=True)

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
        context={'cards': fotografias, 'categorias': categorias}
    )