# Generated by Django 4.0.4 on 2022-06-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_report_delete_reports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_type',
            field=models.CharField(choices=[('rad', 'Radiology'), ('med', 'Medical')], max_length=100, verbose_name='Report Type'),
        ),
    ]