# Generated by Django 3.2.8 on 2023-11-18 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equations', '0003_standardsoilrxelements_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='standardsoilrxelements',
            options={'ordering': ['order']},
        ),
    ]
