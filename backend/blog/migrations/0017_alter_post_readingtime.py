# Generated by Django 4.2.6 on 2023-11-02 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_delete_contact_alter_comment_member_delete_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='readingTime',
            field=models.PositiveIntegerField(),
        ),
    ]
