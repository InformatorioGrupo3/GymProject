# Generated by Django 3.1.6 on 2021-03-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='seleccionable',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]
