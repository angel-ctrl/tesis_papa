# Generated by Django 3.2.9 on 2021-11-24 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0003_alter_ordenes_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenes',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
