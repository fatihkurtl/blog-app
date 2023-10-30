# Generated by Django 4.2.6 on 2023-10-17 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_post_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('tr', 'Turkish')], default='tr', max_length=2),
        ),
    ]
