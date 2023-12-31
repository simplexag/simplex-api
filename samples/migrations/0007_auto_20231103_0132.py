# Generated by Django 3.2.8 on 2023-11-03 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0006_alter_samplessoil_sample_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sampleevent',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='standardsoilelements',
            name='source',
            field=models.CharField(choices=[('MODUS', 'Modus')], default='MODUS', max_length=10),
        ),
        migrations.AddField(
            model_name='standardsoilextractions',
            name='source',
            field=models.CharField(choices=[('MODUS', 'Modus')], default='MODUS', max_length=10),
        ),
    ]
