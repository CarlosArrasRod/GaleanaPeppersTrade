# Generated by Django 5.0.7 on 2024-08-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipas', '0002_alter_pipas_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='pipas',
            name='bombac',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
    ]
