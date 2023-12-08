# Generated by Django 3.2.8 on 2023-12-08 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equations', '0016_auto_20231129_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardsoilrxelements',
            name='default_max_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='standardsoilrxelements',
            name='default_min_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='standardsoilrxelements',
            name='default_rate_unit',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='standardsoilrxelements',
            name='default_switch_rate',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
