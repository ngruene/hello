# Generated by Django 4.2.16 on 2024-09-26 09:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_subtitle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='subtitle',
            new_name='edit_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.CharField(max_length=200),
        ),
    ]
