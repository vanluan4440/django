# Generated by Django 3.2.9 on 2021-12-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0002_class_a_createdby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_a',
            name='createdBy',
            field=models.IntegerField(),
        ),
    ]
