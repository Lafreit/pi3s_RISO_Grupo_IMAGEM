from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu usuário",
            }
        ),
        error_messages={"required": "Informe o usuário."},
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha",
            }
        ),
        error_messages={"required": "Informe a senha."},
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise ValidationError("Usuário não encontrado.")
            else:
                user_auth = authenticate(username=username, password=password)

                if not user.is_active:
                    raise forms.ValidationError('Usuário inativo, entre em contato com o administrador.')

                if user_auth is None:
                    raise forms.ValidationError('Senha incorreta para o usuario informado.')

                self.user = user

        return cleaned_data
