# Generated by Django 4.0.4 on 2022-06-04 14:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_alter_doctor_options_alter_patient_options_and_more'),
        ('core', '0002_referal_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referal',
            name='body',
            field=models.CharField(choices=[('ab', 'Abdomen'), ('ch', 'Chest'), ('pl', 'Pelvis'), ('ue', 'Upper Extremities'), ('le', 'Lower Extremities'), ('sp', 'Spine'), ('hnf', 'Head, Neck and Face'), ('ot', 'Others')], default='ot', max_length=100, verbose_name='Body Location'),
        ),
        migrations.AlterField(
            model_name='referal',
            name='rad_types',
            field=models.CharField(choices=[('x', 'X-Ray'), ('ct', 'CT-Scan'), ('mri', 'MRI'), ('ot', 'Others')], default='ot', max_length=100, verbose_name='Test Type'),
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(choices=[('x', 'X-Ray'), ('ct', 'CT-Scan'), ('mri', 'MRI'), ('ot', 'Others')], max_length=100, verbose_name='Report Type')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='report_doctor', to='register.doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_patient', to='register.patient')),
            ],
        ),
    ]