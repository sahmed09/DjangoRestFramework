# Generated by Django 3.2.7 on 2021-10-28 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20211027_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderstatus',
            name='status',
        ),
    ]