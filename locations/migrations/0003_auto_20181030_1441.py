# Generated by Django 2.1.2 on 2018-10-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20181027_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationvisit',
            name='flags',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='locationvisit',
            name='visit_time',
            field=models.DateTimeField(null=True),
        ),
    ]
