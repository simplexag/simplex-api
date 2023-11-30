# Generated by Django 3.2.8 on 2023-11-29 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equations', '0015_auto_20231129_0321'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='standardrxcrops',
            options={'permissions': (('can_undelete', 'Can undelete this object'),)},
        ),
        migrations.RemoveField(
            model_name='equationcrops',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='equationcrops',
            name='deleted_by_cascade',
        ),
        migrations.RemoveField(
            model_name='equationelement',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='equationelement',
            name='deleted_by_cascade',
        ),
        migrations.RemoveField(
            model_name='equationsets',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='equationsets',
            name='deleted_by_cascade',
        ),
        migrations.RemoveField(
            model_name='standardrxcrops',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='standardrxcrops',
            name='deleted_by_cascade',
        ),
        migrations.RemoveField(
            model_name='standardsoilrxelements',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='standardsoilrxelements',
            name='deleted_by_cascade',
        ),
        migrations.AddField(
            model_name='equationcrops',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='equationelement',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='equationsets',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='standardrxcrops',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='standardsoilrxelements',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
    ]
