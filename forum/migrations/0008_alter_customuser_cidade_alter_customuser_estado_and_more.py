# Generated by Django 4.1.4 on 2022-12-27 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0007_alter_customuser_nome_completo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="cidade",
            field=models.CharField(default=" ", max_length=50),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="estado",
            field=models.CharField(default=" ", max_length=2),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="nome_social",
            field=models.CharField(default=" ", max_length=50),
        ),
    ]