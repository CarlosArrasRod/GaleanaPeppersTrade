# Generated by Django 5.0.7 on 2024-08-05 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('weight', '0004_alter_weight_fecha_alter_weight_nombrechof_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaciado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hdecomiezov', models.FloatField()),
                ('hdefinalizacionv', models.FloatField()),
                ('hdecomiezobanda', models.TimeField()),
                ('hdefinalizacionbanda', models.TimeField()),
                ('tiempovaciado', models.TimeField()),
                ('tiempodebanda', models.TimeField()),
                ('weight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaciados', to='weight.weight')),
            ],
        ),
    ]
