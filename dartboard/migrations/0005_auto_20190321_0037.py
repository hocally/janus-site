# Generated by Django 2.1.7 on 2019-03-21 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dartboard', '0004_auto_20190305_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='decision',
            name='author',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='decision',
        ),
        migrations.DeleteModel(
            name='Decision',
        ),
    ]
