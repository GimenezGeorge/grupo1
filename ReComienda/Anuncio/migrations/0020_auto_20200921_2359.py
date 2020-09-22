# Generated by Django 3.1 on 2020-09-22 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anuncio', '0019_auto_20200920_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anuncio_trans',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='anuncio_trans',
            name='tel',
        ),
        migrations.AddField(
            model_name='anuncio_trans',
            name='E_mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='anuncio_trans',
            name='telefono',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contratista',
            name='E_mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contratista',
            name='telefono',
            field=models.CharField(max_length=20, null=True, verbose_name='Nro Telefono'),
        ),
    ]