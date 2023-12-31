# Generated by Django 3.2.8 on 2023-11-23 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equations', '0010_auto_20231123_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equationcrops',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equation_crops', to='equations.equationsets'),
        ),
        migrations.AlterField(
            model_name='equationelement',
            name='crop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equation_elements', to='equations.equationcrops'),
        ),
    ]
