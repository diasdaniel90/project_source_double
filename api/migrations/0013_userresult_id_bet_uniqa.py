# Generated by Django 2.1.4 on 2023-03-15 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_userresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresult',
            name='ID_bet_uniqa',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
