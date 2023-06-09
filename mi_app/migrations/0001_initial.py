# Generated by Django 4.2 on 2023-04-13 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pausas_Activas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('hora', models.DateField()),
                ('fecha', models.DateTimeField()),
                ('duracion', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Activdades_fisicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descipcion', models.CharField(max_length=50)),
                ('act_usu', models.ManyToManyField(to='mi_app.usuario')),
            ],
        ),
    ]
