# Generated by Django 4.0.4 on 2022-06-26 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_referal_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='referal',
            name='radcheck',
            field=models.BooleanField(default=False),
        ),
    ]
