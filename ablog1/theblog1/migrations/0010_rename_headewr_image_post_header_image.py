# Generated by Django 5.0.1 on 2024-02-29 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog1', '0009_post_headewr_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='headewr_image',
            new_name='header_image',
        ),
    ]
