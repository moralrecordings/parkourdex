# Generated by Django 2.1.2 on 2018-11-04 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0005_auto_20181103_0915'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='locationvisit',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='locationvisit',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='locationvisit',
            name='location',
        ),
        migrations.RemoveField(
            model_name='locationvisit',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='locationvisit',
            name='user',
        ),
        migrations.DeleteModel(
            name='LocationVisit',
        ),
    ]