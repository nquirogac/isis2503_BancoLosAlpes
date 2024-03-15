# Generated by Django 4.1.13 on 2024-03-15 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('lastName', models.CharField(max_length=150)),
                ('document', models.BigIntegerField(primary_key=True, serialize=False)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('income', models.FloatField()),
                ('debt', models.FloatField()),
                ('economicActivity', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
