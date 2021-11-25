# Generated by Django 3.2.9 on 2021-11-24 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('seccion', models.CharField(max_length=20)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(upload_to='')),
                ('stock', models.IntegerField()),
                ('vendedor', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
                'db_table': 'productos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ordenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprador', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('code_hash', models.CharField(default='none', max_length=250)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion1.productos')),
            ],
            options={
                'verbose_name': 'ordenes',
                'verbose_name_plural': 'ordenes',
                'db_table': 'ordenes',
                'ordering': ['id'],
            },
        ),
    ]
