# Generated by Django 3.2.8 on 2024-01-01 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20231013_0153'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='farm',
            name='farm_unique_if_not_deleted',
        ),
        migrations.RemoveConstraint(
            model_name='field',
            name='field_unique_if_not_deleted',
        ),
        migrations.RemoveConstraint(
            model_name='grower',
            name='grower_unique_if_not_deleted',
        ),
    ]
