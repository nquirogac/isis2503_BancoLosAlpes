# Generated by Django 3.2.6 on 2024-03-14 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitud',
            old_name='apellido',
            new_name='operation',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='id',
            new_name='userId',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='email',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='fecha_nacimiento',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='telefono',
        ),
    ]
