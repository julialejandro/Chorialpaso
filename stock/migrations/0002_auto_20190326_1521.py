# Generated by Django 2.1.7 on 2019-03-26 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id_categoria',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='formato',
            name='id_formato',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='id_proveedor',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
