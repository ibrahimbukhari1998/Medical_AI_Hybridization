# Generated by Django 4.0.4 on 2022-06-21 23:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_tempstorage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempstorage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='temp/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])]),
        ),
    ]
