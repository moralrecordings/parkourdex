# Generated by Django 2.1.2 on 2018-11-03 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20181030_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='locations', to='locations.Feature'),
        ),
    ]
