# Generated by Django 2.1.7 on 2019-03-27 04:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dartboard', '0005_auto_20190321_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
