# Generated by Django 2.1.7 on 2019-03-27 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dartboard', '0006_choice_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='timestamp',
            field=models.DateTimeField(blank=True, max_length=200),
        ),
    ]
