# Generated by Django 3.2.9 on 2022-01-17 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_lesson_create_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='create_by',
            field=models.IntegerField(),
        ),
    ]
