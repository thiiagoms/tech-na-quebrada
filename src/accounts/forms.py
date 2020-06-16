from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)

User = get_user_model()

class VolunteerLoginForm(forms.Form):

    username = forms.CharField(
        label="Digite seu nome de usuário",
        widget=forms.TextInput(attrs={ 'placeholder': 'Digite seu nome de usuário:' }
    ))
    password = forms.CharField(
        label="Digite sua senha",
        widget=forms.PasswordInput(attrs={ 'placeholder': 'Digite sua senha:' }
    ))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError(
                  "Usuário não existente"
                )
            if not user.check_password(password):
                raise forms.ValidationError(
                  "Senha incorreta"
                )
            if not user.is_active:
                raise forms.ValidationError(
                  "Usuário não está ativo"
                )
        return super(VolunteerLoginForm, self).clean(*args, **kwargs)

class VolunteerRegisterForm(forms.ModelForm):

    username = forms.CharField(
       label = "Informe seu nome de usuário: ",
       widget = forms.TextInput( attrs = { 'placeholder': "Nome de usuário necessário para entrar na plataforma" })
    )
    first_name = forms.CharField(
       label = "Informe seu primeiro nome: ",
       widget = forms.TextInput(attrs = { 'placeholder': "Informe o seu primeiro nome" })
    )
    last_name = forms.CharField(
       label = "Informe seu último nome",
       widget = forms.TextInput(attrs = { 'placeholder': "Informe seu último nome" })
    )
    email = forms.EmailField(
       label = "Informe seu e-mail: ",
       widget = forms.EmailInput(attrs = { 'placeholder': "Informe o endereço de e-mail válido" })
    )
    email2 = forms.EmailField(
       label = "Confirme seu e-mail: ",
       widget = forms.EmailInput(attrs = { 'placeholder': "Informe novamente seu e-mail" })
    )
    password = forms.CharField(
        label="Digite sua senha: ",
        widget=forms.PasswordInput( attrs = { 'placeholder' : "Informa uma senha válida" })
    )
    image = forms.ImageField(label="Escolha seu avatar: ")

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'email2',
            'password',
            'image'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError(
              "Endereço não confere com o original"
            )
        email_exists = User.objects.filter(email=email)
        if email_exists.exists():
            raise forms.ValidationError("Endereço de email já existe!!")

        return super(VolunteerRegisterForm, self).clean(*args, **kwargs)

class VolunteerEditForm(forms.ModelForm):

    username = forms.CharField(
        label="Nome de usuário: "
    )
    first_name = forms.CharField(
        label="Nome:  ",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Informe seu primeiro nome"
            }
        )
    )
    last_name = forms.CharField(
        label="Sobrenome: ",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Informe seu sobrenome"
            }
        )
    )
    email = forms.EmailField(
        label="E-mail: ",
        widget=forms.EmailInput(
            attrs={
                'placeholder': "Informe seu novo endereço de e-mail"
            }
        )
    )
    password = forms.CharField(
        label="Digite sua senha: ",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Digite sua nova senha"
        })
    )
    password2 = forms.CharField(
        label="Confirmar nova senha: ",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Confirmar sua nova senha"
            }
        )
    )
  
    def __init__(self, *args, **kwargs):
        super(VolunteerEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled=True

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password2'
        ]
