# Generated by Django 4.2.6 on 2023-11-10 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe_emails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribevisitors',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='subscribevisitors',
            name='update_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
