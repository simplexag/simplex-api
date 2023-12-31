# Generated by Django 3.2.8 on 2023-09-30 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20230930_0205'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='organization',
            name='organization_unique_if_not_deleted',
        ),
        migrations.AddConstraint(
            model_name='organization',
            constraint=models.UniqueConstraint(condition=models.Q(('is_deleted', False)), fields=('account', 'name'), name='organization_unique_if_not_deleted'),
        ),
    ]
