# Generated by Django 5.0.7 on 2024-07-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_category_options_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.FileField(blank=True, upload_to='category/icons/'),
        ),
    ]
