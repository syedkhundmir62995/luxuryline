# Generated by Django 4.0 on 2022-01-24 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0013_quotationamount_quotationclient_quotationitem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='client_name',
        ),
        migrations.AddField(
            model_name='quotationnumber',
            name='clientaddress',
            field=models.TextField(default='Client Address', max_length=1000),
        ),
        migrations.AddField(
            model_name='quotationnumber',
            name='clientname',
            field=models.CharField(default='Client Name', max_length=1000),
        ),
        migrations.DeleteModel(
            name='quotationclient',
        ),
    ]