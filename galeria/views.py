from django.shortcuts import get_object_or_404, render
from galeria.models import Fotografia


# Create your views here.
def index(request):
    fotografias = Fotografia.objects.filter(publicada=True)

    categorias = []
    for conjunto in Fotografia.OPCOES_DE_CATEGORIA:
        categorias.append(conjunto[1])

    return render(
        request,
        template_name='galeria/index.html',
        context={'cards': fotografias, 'categorias': categorias}
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
    return render(
        request,
        template_name='galeria/buscar.html',
        #context={'fotografia': fotografia}
    )