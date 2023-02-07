from django.shortcuts import render

# Create your views here.
def index(request):
    return render(
        request,
        template_name='galeria/index.html',
        context={'numero_de_cards': [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]}
    )

def imagem(request):
    return render(request, 'galeria/imagem.html')