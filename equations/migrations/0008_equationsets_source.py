# Generated by Django 3.2.8 on 2023-11-20 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equations', '0007_auto_20231120_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='equationsets',
            name='source',
            field=models.CharField(choices=[('U', 'User'), ('V', 'University'), ('L', 'Lab')], default='U', max_length=1),
        ),
    ]