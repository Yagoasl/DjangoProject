# Generated by Django 4.0.6 on 2022-08-10 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0004_livroreceitas_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='livroreceitas',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
