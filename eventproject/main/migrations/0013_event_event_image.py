# Generated by Django 4.1.7 on 2023-02-26 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]