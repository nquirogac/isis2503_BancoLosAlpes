# Generated by Django 4.1.13 on 2024-03-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('lastName', models.CharField(max_length=150)),
                ('document', models.BigIntegerField(primary_key=True, serialize=False)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
