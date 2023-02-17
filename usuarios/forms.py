from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: João da Silva",
            }
        ),
    )
    senha=forms.CharField(
        label='Senha',
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha",
            }
        ),
    )


class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome completo',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: João da Silva",
            }
        ),
    )
    email=forms.EmailField(
        label='Email',
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: joaosilva@js1.com"
            }
        ),
    )
    senha_1=forms.CharField(
        label='Senha',
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha",
            }
        ),
    )
    senha_2=forms.CharField(
        label='Confirmação de senha',
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha mais uma vez",
            }
        ),
    )
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Espaços não são permitidos nesse campo")
            else:
                return nome

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')
        if senha_1 != senha_2:
            raise forms.ValidationError('As senhas não correspondem')
        else:
            return senha_2


class FavoritosForms(forms.Form):
    fotografia_id=forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "visible": False,
            }
        ),
    )
    is_favorito=forms.BooleanField(
        required=True
    )