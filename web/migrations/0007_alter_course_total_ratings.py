# Generated by Django 5.0.7 on 2024-07-29 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_course_total_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='total_ratings',
            field=models.IntegerField(default=0),
        ),
    ]
