# Generated by Django 4.2.6 on 2023-11-09 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_remove_socialmedialink_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmedialink',
            old_name='twitter_url',
            new_name='x_url',
        ),
    ]
