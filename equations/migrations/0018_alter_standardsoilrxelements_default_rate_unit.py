# Generated by Django 3.2.8 on 2023-12-08 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equations', '0017_auto_20231208_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardsoilrxelements',
            name='default_rate_unit',
            field=models.CharField(default='lbs/ac', max_length=20),
            preserve_default=False,
        ),
    ]
