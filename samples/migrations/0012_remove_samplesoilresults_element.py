# Generated by Django 3.2.8 on 2023-11-09 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0011_auto_20231105_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='samplesoilresults',
            name='element',
        ),
    ]
