# Generated by Django 5.1.2 on 2024-11-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='corrida_pessoa',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(db_column='NOME')),
                ('sobrenome', models.TextField(db_column='SOBRENOME')),
                ('genero', models.TextField(db_column='GENERO')),
                ('dtNasc', models.DateField(db_column='DATA NASC')),
                ('distancia', models.TextField(db_column='DISTANCIA')),
            ],
            options={
                'db_table': 'corrida_pessoa',
                'ordering': ['user_id'],
                'managed': True,
            },
        ),
    ]
