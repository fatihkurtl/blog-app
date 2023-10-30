# Generated by Django 4.2.6 on 2023-10-18 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.member', to_field='userName'),
        ),
    ]
