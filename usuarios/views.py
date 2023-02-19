from django.shortcuts import redirect, render
from usuarios.forms import CadastroForms, FavoritosForms, LoginForms
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from usuarios.models import Favoritos
from galeria.models import Fotografia

# Create your views here.
def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha,
            )

            if usuario is None:
                messages.error(request, f'O usuário {nome} não existe, tente se cadastrar primeiro')
                return redirect('login')

            auth.login(
                request,
                usuario
            )
            messages.success(request, f'Usuário {nome} logado com sucesso!')
            return redirect('index')

    return render(
        request,
        template_name='usuarios/login.html',
        context={'form': form}
    )

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        # Vai pegar todas as informações preenchidas no formulário
        # pelo cliente e enviar para a nossa classe CadastroForms
        form = CadastroForms(request.POST)

        if form.is_valid():
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            # Vamos agora verificar se o nome já está presente no nosso banco
            # de usuários
            # Estamos usando "username" como nome do campo, pois estamos
            # usando para esse cadastro a mesma tabela de onde cadastramos
            # nossos administradores: db.sqlite3 > auth.user
            if User.objects.filter(username=nome).exists():
                # Se já existir, então reseta a página de cadastro
                messages.error(request, f'O usuário {nome} já está cadastrado, tente cadastrar outro nome ou fazer o login')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username = nome,
                email = email,
                password = senha,
            )
            usuario.save()

            messages.success(request, f'Usuário {nome} cadastrado com sucesso!')
            return redirect('login')
        else:
            return render(
                request,
                template_name='usuarios/cadastro.html',
                context={'form': form}
            )


    if request.method == 'GET':
        return render(
            request,
            template_name='usuarios/cadastro.html',
            context={'form': form}
        )

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')

@csrf_exempt
def favorito(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Você precisa estar logado para adicionar fotos aos favoritos')
            redirect('login')

        # Copiando o POST para converter o valor da variável "is_favorito"
        # de numérico para Booleano
        post = request.POST.copy()
        if post['is_favorito'] == 0 or post['is_favorito'] == '0':
            post.update({'is_favorito': False})
        else:
            post.update({'is_favorito': True})
        
        # Atualizando o valor do POST Request
        request.POST = post
        print(post)

        # Passando os valores do POST para nosso objeto FavoritosForms
        # Como nossos campos de "usuario_id" e "fotografia_id" são
        # ForeignKeys, então devemos passar os objetos para dentro
        # do nosso Favoritos Model para podermos criar um objeto
        # ao invés de passar apenas os valores vindos do POST
        form = FavoritosForms(request.POST)
        usuario = User.objects.get(id=request.user.id)
        fotografia = Fotografia.objects.get(id=form['fotografia_id'].value())
        is_favorito = form['is_favorito'].value()

        # Filtrando o usuário e a fotografia na qual o usuário deu like
        # para ver se ela já existe no banco de dados dos Favoritos
        favoritos = Favoritos.objects.filter(usuario=usuario.id).filter(fotografia=fotografia.id)

        # Se já existir no banco, precisamos atualizar o valor
        if favoritos.exists():
            favoritos.update(is_favorito = is_favorito)

        # Senão vamos criar uma nova linha
        if not favoritos.exists():
            favoritos = Favoritos(
                usuario = usuario,
                fotografia = fotografia,
                is_favorito = is_favorito,
            )
            favoritos.save()

        return redirect('index')