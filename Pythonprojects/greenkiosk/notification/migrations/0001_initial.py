# Generated by Django 4.2.2 on 2023-06-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateField()),
                ('recipient', models.CharField(max_length=32)),
                ('type_of_notification', models.TextField()),
            ],
        ),
    ]
