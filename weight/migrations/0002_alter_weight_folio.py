# Generated by Django 5.0.7 on 2024-07-19 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='folio',
            field=models.CharField(max_length=10, verbose_name='Folio'),
        ),
    ]
