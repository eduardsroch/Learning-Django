# Generated by Django 5.0.3 on 2024-04-11 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_descricao_delete_autor_delete_editora'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='imagem',
            field=models.TextField(null=True),
        ),
    ]