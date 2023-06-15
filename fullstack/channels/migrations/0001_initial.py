# Generated by Django 4.2.2 on 2023-06-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='channels/')),
                ('channelName', models.CharField(max_length=100)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('article_title', models.CharField(max_length=100)),
                ('article_description', models.TextField()),
            ],
        ),
    ]
