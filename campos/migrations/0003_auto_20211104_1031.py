# Generated by Django 3.2.9 on 2021-11-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campos', '0002_campos_tipo_noticia'),
    ]

    operations = [
        migrations.AddField(
            model_name='campos',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='inages/'),
        ),
        migrations.AddField(
            model_name='campos',
            name='imagemheight',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='campos',
            name='imagemwidth',
            field=models.PositiveIntegerField(default=0),
        ),
    ]