# Generated by Django 3.2.5 on 2022-01-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_auto_20220114_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='vat',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]