# Generated by Django 4.1.3 on 2022-11-24 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]
