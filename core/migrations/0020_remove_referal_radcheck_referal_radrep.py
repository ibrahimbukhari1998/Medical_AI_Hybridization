# Generated by Django 4.0.4 on 2022-06-26 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_referal_radcheck'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referal',
            name='radcheck',
        ),
        migrations.AddField(
            model_name='referal',
            name='radrep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.radreport'),
        ),
    ]
