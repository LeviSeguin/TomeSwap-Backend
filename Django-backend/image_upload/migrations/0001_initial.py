# Generated by Django 4.1.6 on 2024-03-17 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=255)),
                ('categories', models.CharField(max_length=255)),
                ('username', models.CharField(default='test', max_length=255)),
                ('listingid', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
