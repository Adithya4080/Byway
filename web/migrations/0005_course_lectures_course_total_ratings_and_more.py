# Generated by Django 5.0.7 on 2024-07-29 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_course_original_price_alter_course_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lectures',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='total_ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_by',
            field=models.CharField(default='Unknown', max_length=25),
        ),
        migrations.AlterField(
            model_name='course',
            name='discount_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='languages',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='original_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='course',
            name='ratings',
            field=models.FloatField(default=0.0),
        ),
    ]
