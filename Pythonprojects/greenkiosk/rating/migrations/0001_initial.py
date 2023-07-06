# Generated by Django 4.2.2 on 2023-06-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_message', models.TextField()),
                ('sender', models.CharField(max_length=32)),
                ('star_rating', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
