# Generated by Django 2.1.4 on 2023-03-10 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20230310_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverresult',
            name='timestamp',
            field=models.FloatField(),
        ),
    ]
