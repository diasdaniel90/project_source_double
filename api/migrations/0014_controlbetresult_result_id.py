# Generated by Django 2.1.4 on 2023-03-18 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_userresult_id_bet_uniqa'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlbetresult',
            name='result_id',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]