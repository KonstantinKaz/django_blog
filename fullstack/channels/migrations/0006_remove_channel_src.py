# Generated by Django 4.2.2 on 2023-06-14 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0005_alter_channel_image_alter_channel_src'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='src',
        ),
    ]
