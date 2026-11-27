from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Camisa12", "0009_lojas_iniciais"),
    ]

    operations = [
        migrations.AddField(
            model_name="oferta",
            name="imagem",
            field=models.URLField(blank=True, help_text="Foto do produto anunciado por esta loja (se vazio, usa a foto do produto)"),
        ),
    ]
