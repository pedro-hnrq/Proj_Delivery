# Generated by Django 4.0.6 on 2022-07-11 22:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CupomDesconto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8, unique=True)),
                ('desconto', models.FloatField()),
                ('usos', models.IntegerField(default=0)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 11, 19, 35, 12, 556376)),
        ),
    ]
