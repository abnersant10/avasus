# Generated by Django 4.1.4 on 2023-01-03 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0002_topico_estado"),
    ]

    operations = [
        migrations.AddField(
            model_name="resposta",
            name="nome_autor",
            field=models.CharField(default=" ", max_length=50),
        ),
        migrations.AddField(
            model_name="subforum",
            name="nome_autor",
            field=models.CharField(default=" ", max_length=50),
        ),
        migrations.AddField(
            model_name="topico",
            name="nome_autor",
            field=models.CharField(default=" ", max_length=50),
        ),
    ]
