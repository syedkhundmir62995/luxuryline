# Generated by Django 4.0 on 2022-01-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0004_alter_supplier_vat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='vat',
            field=models.CharField(blank=True, default=0, max_length=200),
        ),
    ]
