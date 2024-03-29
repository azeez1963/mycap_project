# Generated by Django 4.2.11 on 2024-03-25 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_store_owner_store_location_store_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='products',
        ),
        migrations.AlterField(
            model_name='store',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
