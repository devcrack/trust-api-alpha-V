# Generated by Django 3.0.6 on 2020-05-30 02:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Gelocation', '0001_initial'),
        ('TankerTruck', '0001_initial'),
        ('Clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('place_reference', models.CharField(blank=True, max_length=300, null=True)),
                ('commitment_date', models.DateTimeField()),
                ('folio', models.CharField(max_length=300)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client_order', to='Clients.Client')),
                ('tanker_truck', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tanker_trucks_orders', to='TankerTruck.TankerTruck')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('folio', models.CharField(max_length=300)),
                ('volumen', models.IntegerField(default=-1)),
                ('date_time_start', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_time_end', models.DateTimeField(default=None)),
                ('density', models.DecimalField(decimal_places=3, default=None, max_digits=7)),
                ('mass', models.DecimalField(decimal_places=3, default=None, max_digits=7)),
                ('temperature', models.DecimalField(decimal_places=3, default=None, max_digits=4)),
                ('totalizer_volume', models.IntegerField(default=-1)),
                ('amount_purchase', models.DecimalField(decimal_places=2, max_digits=7)),
                ('geodata', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='geodata_service', to='Gelocation.Geolocation')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order_service', to='OrderServices.Order')),
                ('tanker_truck', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tanker_truck_service', to='TankerTruck.TankerTruck')),
            ],
        ),
    ]
