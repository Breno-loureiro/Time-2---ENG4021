import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Camisa12", "0007_alter_produto_categoria"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Loja",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=100, unique=True)),
                ("especialidade", models.CharField(blank=True, max_length=100)),
                ("site", models.URLField(blank=True)),
                ("verificada", models.BooleanField(default=False)),
            ],
            options={"db_table": "Loja", "ordering": ["nome"], "managed": True},
        ),
        migrations.CreateModel(
            name="Oferta",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("preco", models.DecimalField(decimal_places=2, max_digits=10)),
                ("frete", models.DecimalField(decimal_places=2, default=0, help_text="Deixe 0 para frete grátis", max_digits=8)),
                ("link", models.URLField(blank=True, help_text="Página do produto no site da loja")),
                ("loja", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="ofertas", to="Camisa12.loja")),
                ("produto", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="ofertas", to="Camisa12.produto")),
            ],
            options={"db_table": "Oferta", "ordering": ["preco"], "managed": True},
        ),
        migrations.AddConstraint(
            model_name="oferta",
            constraint=models.UniqueConstraint(fields=("produto", "loja"), name="uma_oferta_por_loja"),
        ),
        migrations.CreateModel(
            name="Avaliacao",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nota", models.PositiveSmallIntegerField(choices=[(1, "1 estrela"), (2, "2 estrelas"), (3, "3 estrelas"), (4, "4 estrelas"), (5, "5 estrelas")])),
                ("comentario", models.TextField(blank=True)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                ("produto", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="avaliacoes", to="Camisa12.produto")),
                ("usuario", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="avaliacoes", to=settings.AUTH_USER_MODEL)),
            ],
            options={"db_table": "Avaliacao", "ordering": ["-criado_em"], "managed": True},
        ),
        migrations.AddConstraint(
            model_name="avaliacao",
            constraint=models.UniqueConstraint(fields=("produto", "usuario"), name="uma_avaliacao_por_usuario"),
        ),
    ]
