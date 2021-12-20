# Generated by Django 3.2.9 on 2021-12-12 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=255)),
                ('author', models.BooleanField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
