# Generated by Django 5.0 on 2023-12-28 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='content',
            field=models.TextField(default=''),
        ),
    ]