# Generated by Django 4.1.7 on 2023-02-21 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_event_attendess'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='myEventUser',
            new_name='EventUser',
        ),
    ]
