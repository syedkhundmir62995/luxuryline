# Generated by Django 4.0 on 2022-01-24 16:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0014_remove_quotation_client_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='demo',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='quotation',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
