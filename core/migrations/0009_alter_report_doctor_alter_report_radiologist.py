# Generated by Django 4.0.4 on 2022-06-07 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_alter_customuser_first_name'),
        ('core', '0008_remove_radreport_multi_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='report_doctor', to='register.doctor'),
        ),
        migrations.AlterField(
            model_name='report',
            name='radiologist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='report_radiologist', to='register.radiologist'),
        ),
    ]
