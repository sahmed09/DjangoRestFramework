# Generated by Django 3.2.7 on 2021-10-29 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopbranchproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
