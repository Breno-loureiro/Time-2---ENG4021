"""
Cadastra no banco as camisas de futebol que ficavam escritas direto no
HTML antigo (Telas html/futebol.html) e que não aparecem na página nova,
porque ela só mostra o que está no banco.

Mantém os mesmos nomes e preços do HTML antigo. Fluminense I e Flamengo I
ficam de fora porque já existem no banco (Camisa Fluminense e Camisa
Flamengo). Sem fotos, como no HTML antigo.

Pode rodar mais de uma vez: produtos com o mesmo nome não são duplicados.

Uso:  python manage.py restaurar_camisas_antigas
"""
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from Camisa12.models import NotaConservacao, Produto, Tamanho, Time

# (time, nome como era no HTML antigo, modelo, preço)
CAMISAS = [
    ("Fluminense", "Fluminense II 2026 • Visitante", "Visitante", "379.90"),
    ("Fluminense", "Fluminense III 2026 • Terceira", "Terceira", "339.90"),
    ("Palmeiras", "Palmeiras I 2026 • Titular", "Titular", "349.90"),
    ("Palmeiras", "Palmeiras II 2026 • Visitante", "Visitante", "329.90"),
    ("Palmeiras", "Palmeiras III 2026 • Terceira", "Terceira", "369.90"),
    ("São Paulo", "São Paulo I 2026 • Titular", "Titular", "329.90"),
    ("Grêmio", "Grêmio II 2026 • Visitante", "Visitante", "319.90"),
    ("Internacional", "Internacional I 2026 • Titular", "Titular", "329.90"),
    ("Internacional", "Internacional II 2026 • Visitante", "Visitante", "309.90"),
    ("Vasco da Gama", "Vasco da Gama I 2026 • Titular", "Titular", "329.90"),
    ("Corinthians", "Corinthians I 2026 • Titular", "Titular", "329.90"),
    ("Botafogo", "Botafogo I 2026 • Titular", "Titular", "319.90"),
    ("Atlético-MG", "Atlético-MG I 2026 • Titular", "Titular", "339.90"),
    ("Cruzeiro", "Cruzeiro I 2026 • Titular", "Titular", "329.90"),
    ("Santos", "Santos I 2026 • Titular", "Titular", "299.90"),
    ("Bahia", "Bahia I 2026 • Titular", "Titular", "319.90"),
    ("Fortaleza", "Fortaleza I 2026 • Titular", "Titular", "289.90"),
    ("Athletico-PR", "Athletico-PR I 2026 • Titular", "Titular", "309.90"),
    ("Sport", "Sport I 2026 • Titular", "Titular", "279.90"),
    ("Ceará", "Ceará I 2026 • Titular", "Titular", "289.90"),
    ("Vitória", "Vitória I 2026 • Titular", "Titular", "279.90"),
    ("Coritiba", "Coritiba I 2026 • Titular", "Titular", "289.90"),
]

SIGLAS = {
    "Fluminense": "FLU", "Palmeiras": "PAL", "São Paulo": "SAO", "Grêmio": "GRE",
    "Internacional": "INT", "Vasco da Gama": "VAS", "Corinthians": "COR",
    "Botafogo": "BOT", "Atlético-MG": "CAM", "Cruzeiro": "CRU", "Santos": "SAN",
    "Bahia": "BAH", "Fortaleza": "FOR", "Athletico-PR": "CAP", "Sport": "SPT",
    "Ceará": "CEA", "Vitória": "VIT", "Coritiba": "CFC",
}

TAMANHOS = ["P", "M", "G", "GG"]


class Command(BaseCommand):
    help = "Cadastra no banco as camisas de futebol que existiam só no HTML antigo."

    def handle(self, *args, **options):
        vendedor = (
            User.objects.filter(is_superuser=True).order_by("id").first()
            or User.objects.order_by("id").first()
        )
        if vendedor is None:
            vendedor = User.objects.create_user(username="camisa12_loja")
            vendedor.set_unusable_password()
            vendedor.save()

        novo = NotaConservacao.objects.filter(nota=5).first()
        tamanhos = [Tamanho.objects.filter(nome=n).first() for n in TAMANHOS]

        criados = 0
        for i, (time_nome, nome, modelo, preco) in enumerate(CAMISAS):
            time, _ = Time.objects.get_or_create(
                nome=time_nome,
                defaults={"sigla": SIGLAS[time_nome], "liga": "Brasileirão"},
            )
            _, criado = Produto.objects.get_or_create(
                nome=nome,
                categoria="FUTEBOL",
                defaults={
                    "preco": Decimal(preco),
                    "modelo": modelo,
                    "ano": 2026,
                    "descricao": f"Camisa {modelo.lower()} do {time_nome} (dados de demonstração).",
                    "ativo": True,
                    "time": time,
                    "tamanho": tamanhos[i % len(tamanhos)],
                    "conservacao": novo,
                    "vendedor": vendedor,
                },
            )
            criados += int(criado)

        self.stdout.write(self.style.SUCCESS(f"{criados} camisas antigas cadastradas."))
