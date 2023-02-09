from django.shortcuts import get_object_or_404, render
from galeria.models import Fotografia


# Create your views here.
def index(request):
    dados = {
        1: {
            "nome": "Nebulosa de Carina",
            "legenda": "webbtelescope.org / NASA / James Webb"
        },
        2: {
            "nome": "Galáxia NGC 1079",
            "legenda": "nasa.org / NASA / Hubble"
        },
        3: {
            "nome": "Núvem Molecular do Camaleão",
            "legenda": "webbtelescope.org / NASA / James Webb"
        },
        4: {
            "nome": "NGC 346",
            "legenda": "webbtelescope.org / NASA / James Webb"
        },
        5: {
            "nome": "JWST Pesquisa do Campo Profundo Extragalático (JADES)",
            "legenda": "webbtelescope.org / NASA / James Webb"
        },
        6: {
            "nome": "Nebulosa do Anel do Sul",
            "legenda": "webbtelescope.org / NASA / James Webb"
        },
        7: {
            "nome": "Pilares da Criação",
            "legenda": "webbtelescope.org / NASA / James Webb"
        },
        8: {
            "nome": "L1527 e Proporestrela",
            "legenda": "webbtelescope.org / NASA / James Webb"
        },
        9: {
            "nome": "Close de Netuno",
            "legenda": "webbtelescope.org / NASA / James Webb"
        },
        10: {
            "nome": "Nebulosa da Tarântula",
            "legenda": "webbtelescope.org / NASA / James Webb"
        },
        11: {
            "nome": "Galáxia Roda de Carro",
            "legenda": "webbtelescope.org / NASA / James Webb"
        },
        12: {
            "nome": "Penhasco Cósmico",
            "legenda": "webbtelescope.org / NASA / James Webb"
        },
        13: {
            "nome": "Quinteto de Stephan",
            "legenda": "webbtelescope.org / NASA / James Webb"
        },
        14: {
            "nome": "Primeiro Campo Profundo do James Webb",
            "legenda": "webbtelescope.org / NASA / James Webb"
        },
        15: {
            "nome": "Visão Multiondas da NGC 1300",
            "legenda": "webbtelescope.org / NASA / James Webb"
        },
    }

    fotografias = Fotografia.objects.all()

    return render(
        request,
        template_name='galeria/index.html',
        context={'cards': fotografias}
    )

def imagem(request, foto_id):
    # pk = Primary Key
    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    return render(
        request,
        template_name='galeria/imagem.html',
        context={'fotografia': fotografia}
    )