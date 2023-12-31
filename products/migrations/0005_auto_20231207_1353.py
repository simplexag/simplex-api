# Generated by Django 3.2.8 on 2023-12-07 13:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('equations', '0016_auto_20231129_0325'),
        ('core', '0009_auto_20231013_0153'),
        ('products', '0004_auto_20231206_0215'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountProductsDefults',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('min', models.FloatField(blank=True, null=True)),
                ('max', models.FloatField(blank=True, null=True)),
                ('switch', models.FloatField(blank=True, null=True)),
                ('unit', models.CharField(max_length=20)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.account')),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='default_rx_element', to='equations.standardsoilrxelements')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.accountproducts')),
            ],
        ),
        migrations.AddField(
            model_name='standardproducts',
            name='application_unit',
            field=models.CharField(default='lbs/ac', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='standardproducts',
            name='bulk_density',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='standardproducts',
            name='bulk_density_unit',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='standardproducts',
            name='bulk_unit',
            field=models.CharField(default='tons/ac', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='standardproducts',
            name='density',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='standardproducts',
            name='density_unit',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='standardproducts',
            name='product_elements',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='standardproducts',
            name='state',
            field=models.CharField(choices=[('S', 'Solid'), ('L', 'Liquid')], default='S', max_length=1),
        ),
        migrations.DeleteModel(
            name='StandardProductElements',
        ),
    ]
