# Generated by Django 3.2.9 on 2021-11-26 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0004_alter_ordenes_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.CharField(max_length=100),
        ),
    ]
