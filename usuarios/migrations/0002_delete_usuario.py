# Generated by Django 4.1.13 on 2024-03-15 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_alter_solicitud_user'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
