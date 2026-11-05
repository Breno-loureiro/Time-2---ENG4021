from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Camisa12.models import Produto


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

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto

        fields = [
            "nome",
            "categoria",
            "marca",
            "modelo",
            "ano",
            "descricao",
            "preco",
            "imagem",
            "tamanho",
            "conservacao",
            "time",
        ]

        labels = {
            "nome": "Nome do produto",
            "categoria": "Categoria",
            "marca": "Marca",
            "modelo": "Modelo",
            "ano": "Ano ou temporada",
            "descricao": "Descrição do produto",
            "preco": "Preço (R$)",
            "imagem": "URL da imagem",
            "tamanho": "Tamanho",
            "conservacao": "Estado de conservação",
            "time": "Time",
        }

        widgets = {
            "nome": forms.TextInput(attrs={
                "placeholder": "Ex.: Camisa Flamengo 2026"
            }),
            "descricao": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "Descreva o produto..."
            }),
            "preco": forms.NumberInput(attrs={
                "min": "0.01",
                "step": "0.01"
            }),
            "ano": forms.NumberInput(attrs={
                "min": "1900",
                "max": "2100"
            }),
            "imagem": forms.URLInput(attrs={
                "placeholder": "https://exemplo.com/imagem.jpg"
            }),
        }

    def clean_preco(self):
        preco = self.cleaned_data["preco"]

        if preco <= 0:
            raise forms.ValidationError(
                "O preço deve ser maior que zero."
            )

        return preco

    def clean_ano(self):
        ano = self.cleaned_data.get("ano")

        if ano is not None and not (1900 <= ano <= 2100):
            raise forms.ValidationError(
                "Informe um ano entre 1900 e 2100."
            )

        return ano