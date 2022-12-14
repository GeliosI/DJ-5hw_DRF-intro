# Generated by Django 4.1.4 on 2022-12-11 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('description', models.CharField(max_length=256, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Датчик',
                'verbose_name_plural': 'Датчики',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField(verbose_name='Температура при измерении')),
                ('data', models.DateField(verbose_name='Дата измерения')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor')),
            ],
            options={
                'verbose_name': 'Измерение',
                'verbose_name_plural': 'Измерения',
                'ordering': ['-data'],
            },
        ),
    ]
