# Generated by Django 3.2.9 on 2021-12-15 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('img', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('course', models.JSONField()),
                ('created_on', models.DateTimeField()),
            ],
        ),
    ]
