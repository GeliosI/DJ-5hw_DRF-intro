# Generated by Django 4.1.4 on 2022-12-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0007_measurement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='image',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Изображение'),
        ),
    ]