# Generated by Django 3.2.5 on 2022-01-26 14:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0019_alter_quotation_goods_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotationnumber',
            name='lastupdated',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
