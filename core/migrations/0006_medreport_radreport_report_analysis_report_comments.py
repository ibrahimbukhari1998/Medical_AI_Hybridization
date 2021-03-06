# Generated by Django 4.0.4 on 2022-06-04 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_report_report_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medreport',
            fields=[
                ('report_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.report')),
                ('visit_reason', models.TextField(null=True, verbose_name='Visit Reason')),
                ('Prescription', models.TextField(null=True, verbose_name='Prescription')),
                ('med_image', models.ImageField(null=True, upload_to='med_reports/')),
            ],
            bases=('core.report',),
        ),
        migrations.CreateModel(
            name='Radreport',
            fields=[
                ('report_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.report')),
                ('test_details', models.TextField(null=True, verbose_name='Test Details')),
                ('rad_image', models.ImageField(null=True, upload_to='rad_reports/')),
            ],
            bases=('core.report',),
        ),
        migrations.AddField(
            model_name='report',
            name='analysis',
            field=models.TextField(null=True, verbose_name='Analysis'),
        ),
        migrations.AddField(
            model_name='report',
            name='comments',
            field=models.TextField(null=True, verbose_name='Comments'),
        ),
    ]
