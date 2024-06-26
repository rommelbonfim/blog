# Generated by Django 3.2.9 on 2021-11-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campos', '0002_auto_20211110_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor_materia', models.CharField(max_length=250, null=True)),
                ('cidade_autor', models.CharField(max_length=250, null=True)),
                ('imagem_autor', models.ImageField(blank=True, null=True, upload_to='imagens/')),
            ],
        ),
        migrations.RemoveField(
            model_name='campos',
            name='autor_materia',
        ),
        migrations.RemoveField(
            model_name='campos',
            name='cidade_autor',
        ),
        migrations.RemoveField(
            model_name='campos',
            name='imagem_autor',
        ),
    ]
