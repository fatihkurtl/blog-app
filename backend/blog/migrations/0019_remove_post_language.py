# Generated by Django 4.2.6 on 2023-11-14 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_post_mdcontent_en_post_mdcontent_tr_post_subtitle_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='language',
        ),
    ]
