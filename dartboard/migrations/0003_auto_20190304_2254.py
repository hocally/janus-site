# Generated by Django 2.1.7 on 2019-03-05 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dartboard', '0002_auto_20190304_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='decision',
        ),
        migrations.AddField(
            model_name='choice',
            name='decision',
            field=models.ForeignKey(help_text='Select a decision for this choice', null=True, on_delete=django.db.models.deletion.SET_NULL, to='dartboard.Decision'),
        ),
    ]
