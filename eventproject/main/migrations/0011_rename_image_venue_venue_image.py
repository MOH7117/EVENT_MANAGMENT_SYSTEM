# Generated by Django 4.1.7 on 2023-02-25 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_venue_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='image',
            new_name='venue_image',
        ),
    ]
