# Generated by Django 5.0.7 on 2024-08-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0005_rename_pesoton_weight_pesokg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='pesolib',
            field=models.FloatField(editable=False),
        ),
    ]
