# Generated by Django 4.1.2 on 2022-10-11 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofdload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kkt',
            name='shop_id',
        ),
        migrations.AddField(
            model_name='kkt',
            name='company_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ofdload.company'),
            preserve_default=False,
        ),
    ]
