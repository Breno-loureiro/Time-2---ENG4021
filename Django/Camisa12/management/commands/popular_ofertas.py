"""
Cria ofertas de exemplo para a apresentação.

Para cada produto ativo que ainda não tem ofertas, cadastra o mesmo
produto em 3 lojas com preços um pouco diferentes, para a página do
produto mostrar a comparação de preços.

Uso:  python manage.py popular_ofertas
"""
from decimal import Decimal

from django.core.management.base import BaseCommand

from Camisa12.models import Loja, Oferta, Produto

# (multiplicador do preço, frete)
VARIACOES = [
    (Decimal("1.00"), Decimal("0")),
    (Decimal("1.07"), Decimal("19.90")),
    (Decimal("1.15"), Decimal("0")),
]


class Command(BaseCommand):
    help = "Cria ofertas de exemplo (3 lojas por produto) para demonstrar a comparação de preços."

    def handle(self, *args, **options):
        lojas = list(Loja.objects.order_by("id"))
        if len(lojas) < 3:
            self.stderr.write("Cadastre pelo menos 3 lojas antes (rode python manage.py migrate).")
            return

        criadas = 0
        for indice, produto in enumerate(Produto.objects.filter(ativo=True).order_by("id")):
            if produto.ofertas.exists():
                continue
            for passo, (fator, frete) in enumerate(VARIACOES):
                loja = lojas[(indice + passo) % len(lojas)]
                Oferta.objects.create(
                    produto=produto,
                    loja=loja,
                    preco=(produto.preco * fator).quantize(Decimal("0.01")),
                    frete=frete,
                )
                criadas += 1

        self.stdout.write(self.style.SUCCESS(f"{criadas} ofertas de exemplo criadas."))
