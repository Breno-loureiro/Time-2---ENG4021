from django.db import migrations

# Mesmas lojas que aparecem na página /lojas/
LOJAS = [
    ("Manto Sagrado Store", "Futebol Brasileiro"),
    ("Giraga Esportes", "NBA / NFL / Futebol"),
    ("Nostalgia FC", "Coleções Vintage"),
    ("Foot Locker Brasil", "Calçados Esportivos"),
    ("Netshoes", "Artigos Esportivos"),
    ("Centauro", "Equipamentos e Roupas"),
    ("Nike.com Brasil", "Nike Exclusivos"),
    ("Adidas Brasil", "Adidas Exclusivos"),
    ("Puma Store BR", "Futebol e Atletismo"),
]


def criar_lojas(apps, schema_editor):
    Loja = apps.get_model("Camisa12", "Loja")
    for nome, especialidade in LOJAS:
        Loja.objects.get_or_create(
            nome=nome,
            defaults={"especialidade": especialidade, "verificada": True},
        )


def apagar_lojas(apps, schema_editor):
    Loja = apps.get_model("Camisa12", "Loja")
    Loja.objects.filter(nome__in=[nome for nome, _ in LOJAS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("Camisa12", "0008_loja_oferta_avaliacao"),
    ]

    operations = [
        migrations.RunPython(criar_lojas, apagar_lojas),
    ]
