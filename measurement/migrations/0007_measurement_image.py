# Generated by Django 4.1.4 on 2022-12-12 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0006_measurement_updated_at_alter_measurement_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
