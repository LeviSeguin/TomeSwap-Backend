# Generated by Django 4.1.6 on 2024-03-17 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0002_rename_book_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='thumbnail',
            field=models.ImageField(default='test', upload_to='listing_thumbnails/'),
        ),
    ]