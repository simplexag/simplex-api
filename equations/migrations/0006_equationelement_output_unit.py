# Generated by Django 3.2.8 on 2023-11-18 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equations', '0005_alter_equationelement_inputs'),
    ]

    operations = [
        migrations.AddField(
            model_name='equationelement',
            name='output_unit',
            field=models.CharField(default='lbs/ac', max_length=20),
            preserve_default=False,
        ),
    ]
