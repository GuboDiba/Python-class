# Generated by Django 4.2.3 on 2023-07-14 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('order', models.TextField()),
                ('location', models.TextField()),
                ('type_of_delivery', models.BooleanField()),
                ('shipment_cost', models.FloatField()),
                ('status', models.TextField()),
                ('delivery_time', models.TimeField()),
                ('orderrs', models.ManyToManyField(to='orders.order')),
            ],
        ),
    ]
