# Generated by Django 4.0.6 on 2024-04-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0002_alter_banda_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='duracao',
            field=models.CharField(max_length=7),
        ),
    ]