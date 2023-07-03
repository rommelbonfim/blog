# Generated by Django 3.2.9 on 2021-11-10 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campos', '0004_auto_20211110_0924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campos',
            name='autor_materia',
        ),
        migrations.AddField(
            model_name='campos',
            name='autor_materia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='campos.autores'),
            preserve_default=False,
        ),
    ]
