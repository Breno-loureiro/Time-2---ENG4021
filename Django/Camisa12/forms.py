from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="E-mail",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Digite seu e-mail",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        labels = {
            "username": "Nome de usuário",
        }

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Digite seu nome de usuário",
                }
            ),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "Já existe uma conta cadastrada com este e-mail."
            )

        return email

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.email = self.cleaned_data["email"]

        if commit:
            usuario.save()

        return usuario