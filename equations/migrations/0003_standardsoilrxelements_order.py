# Generated by Django 3.2.8 on 2023-11-18 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equations', '0002_alter_standardsoilrxelements_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardsoilrxelements',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
