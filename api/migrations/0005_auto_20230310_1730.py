# Generated by Django 2.1.4 on 2023-03-10 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20230310_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serverresult',
            old_name='total_retention',
            new_name='total_retention_eur',
        ),
    ]
