# Generated by Django 4.1.7 on 2023-02-21 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_event_venue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='attendess',
        ),
    ]